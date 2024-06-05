
import os, sys
# ---------copiar estas lineas de codigo en caso de marcar error en las importaciones----------
# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Obtener la ruta del directorio del proyecto (un nivel arriba del directorio actual)
project_dir = os.path.dirname(script_dir)
# Agregar la ruta del proyecto al PYTHONPATH
sys.path.append(project_dir)
# ---------------------------------------------------------------------------------------------

from threading import Thread
import time
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from Api.dobot_api import *
import json
from files.alarm_controller import alarm_controller_list # type: ignore
from files.alarm_servo import alarm_servo_list # type: ignore

LABEL_JOINT = [["J1-", "J2-", "J3-", "J4-"],
               ["J1:", "J2:", "J3:", "J4:"],
               ["J1+", "J2+", "J3+", "J4+"]]

LABEL_COORD = [["X-", "Y-", "Z-", "R-"],
               ["X:", "Y:", "Z:", "R"],
               ["X+", "Y+", "Z+", "R+"]]

LABEL_ROBOT_MODE = {
    1:	"ROBOT_MODE_INIT",
    2:	"ROBOT_MODE_BRAKE_OPEN",
    3:	"",
    4:	"ROBOT_MODE_DISABLED",
    5:	"ROBOT_MODE_ENABLE",
    6:	"ROBOT_MODE_BACKDRIVE",
    7:	"ROBOT_MODE_RUNNING",
    8:	"ROBOT_MODE_RECORDING",
    9:	"ROBOT_MODE_ERROR",
    10:	"ROBOT_MODE_PAUSE",
    11:	"ROBOT_MODE_JOG"
}

class RobotUI(object):

    def __ini__(self):
        self.root = Tk()
        self.root.title("MG400/M1Pro python demo")
        self.root.geometry("900x850")
        #self.root.iconbitmap("imagenes/robot.ico")


        self.global_state = {}

        self.button_list = []

        self.entry_dict = {}

        #conexion al robot
        self.frame_robot = LabelFrame(self.root, text="Robot Connect",
                                      labelanchor="nw", bg="#FFFFFF", width=870, height=120, border=2)
        
        self.label_ip = Label(self.frame_robot, text="IP Adress:")
        self.label_ip.place(rely=0.2, x=10)
        ip_port = StringVar(self.root, value="192.168.1.6")
        self.entry_ip = Entry(self.frame_robot, width=12, textvariable=ip_port)
        self.entry_ip.place(rely=0.2, x=90)

        self.label_dash = Label(self.frame_robot, text="Dashboard Port:")
        self.label_dash.place(rely=0.2, x=210)
        dash_port = IntVar(self.root, value=29999)
        self.entry_dash = Entry(
            self.frame_robot, width=7, textvariable=dash_port)
        self.entry_dash.place(rely=0.2, x=320)

        self.label_move = Label(self.frame_robot, text="Move Port:")
        self.label_move.place(rely=0.2, x=400)
        move_port = IntVar(self.root, value=30003)
        self.entry_feed = Entry(
            self.frame_robot, width=7, textvariable=move_port)
        self.entry_dash.place(rely=0.2, x=480)
        
        self.label_feed = Label(self.frame_robot, text="Feedback Port:")
        self.label_feed.place(rely=0.2, x=580)
        feed_port = IntVar(self.root, value=30004)
        self.entry_feed = Entry(
            self.frame_robot, width=7, textvariable=feed_port)
        self.entry_feed.place(rely=0.2, x=680)

        #Conectar y desconectar
        self.button_connect = self.set_button(master=self.frame_robot,
                                              text="Connect", rely=0.6, x=630, command=self.connect_port)
        self.button_connect["width"] = 10
        self.global_state["connect"] = False

        #Funcion del dashboard
        self.frame_dashboard = LabelFrame(self.root, text="Dashboard Function",
                                          labelanchor="nw", bg="#FFFFFF", pady=10, width=870, height=120, border=2)

        #Habilitar y desabilitar
        self.button_enable = self.set_button(master=self.frame_dashboard,
                                             text="Enable", rely=0.1, x=10, command=self.enable)
        self.button_enable["width"] = 7
        self.global_state["enable"] = False

        #Restablecer el robot/borras errores
        self.set_button(master=self.frame_dashboard,
                        text="Reset Robot", rely=0.1, x=145, command=self.reset_robot)
        self.set_button(master=self.frame_dashboard,
                        text="Clear Error", rely=0.1, x=290, command=self.clear_error)
        
        #Relacion de la velocidad
        self.label_speed = Label(self.frame_dashboard, text="Speed Ratio:")
        self.label_speed.place(rely=0.1, x=430)

        s_value = StringVar(self.root, value="50")
        self.entry_speed = Entry(self.frame_dashboard,
                                 width=6, textvariable=s_value)
        self.entry_speed.place(rely=0.1, x=520)
        self.label_cent = Label(self.frame_dashboard, text="%")
        self.label_cent.place(rely=0.1, x=550)

        self.set_button(master=self.frame_dashboard,
                        text="Confirm", rely=0.1, x=586, command=self.confirm_speed)

        #Salidas digitales
        self.label_digitial = Label(
            self.frame_dashboard, text="Digital Outputs: Index:")
        self.label_digitial.place(rely=0.55, x=10)

        i_value = IntVar(self.root, value="1")
        self.entry_index = Entry(
            self.frame_dashboard, width=5, textvariable=i_value)
        self.entry_index.place(rely=0.55, x=160)

        self.label_status = Label(self.frame_dashboard, text="Status:")
        self.label_status.place(rely=0.55, x=220)

        self.combo_status = ttk.Combobox(self.frame_dashboard, width=5)
        self.combo_status["value"] = ("On", "Off")
        self.combo_status.current(0)
        self.combo_status["state"] = "readonly"
        self.combo_status.place(rely=0.55, x=275)

        self.set_button(self.frame_dashboard, "Confirm",
                        rely=0.55, x=350, command=self.confirm_do)

        #Funciones de moviento
         