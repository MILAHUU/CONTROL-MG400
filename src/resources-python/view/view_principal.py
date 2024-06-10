import os, sys

# ---------copiar estas lineas de codigo en caso de marcar error en las importaciones----------
# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Obtener la ruta del directorio del proyecto (un nivel arriba del directorio actual)
project_dir = os.path.dirname(script_dir)
# Agregar la ruta del proyecto al PYTHONPATH
sys.path.append(project_dir)
# -----------------------------------------------------------------------------------------------

from threading import Thread
import time
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from Api.dobot_api import *
import json
from files.alarm_servo import alarm_servo_list
from files.alarm_controller import alarm_controller_list

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
        self.frame_move = LabelFrame(self.root, text="Move Function", labelanchor="nw",
                                     bg="#FFFFFF", width=870, pady=10, height=130, border=2)

        self.set_move(text="X:", label_value=10,
                      default_value="600", entry_value=40, rely=0.1, master=self.frame_move)
        self.set_move(text="Y:", label_value=110,
                      default_value="-260", entry_value=140, rely=0.1, master=self.frame_move)
        self.set_move(text="Z:", label_value=210,
                      default_value="380", entry_value=240, rely=0.1, master=self.frame_move)
        self.set_move(text="R:", label_value=310,
                      default_value="170", entry_value=340, rely=0.1, master=self.frame_move)

        self.set_button(master=self.frame_move, text="MovJ",
                        rely=0.05, x=410, command=self.movj)
        self.set_button(master=self.frame_move, text="MovL",
                        rely=0.05, x=500, command=self.movl)
        
        self.set_move(text="J1:", label_value=10,
                      default_value="0", entry_value=40, rely=0.5, master=self.frame_move)
        self.set_move(text="J2:", label_value=110,
                      default_value="-20", entry_value=140, rely=0.5, master=self.frame_move)
        self.set_move(text="J3:", label_value=210,
                      default_value="-80", entry_value=240, rely=0.5, master=self.frame_move)
        self.set_move(text="J4:", label_value=310,
                      default_value="30", entry_value=340, rely=0.5, master=self.frame_move)

        self.set_button(master=self.frame_move,
                        text="JointMovJ", rely=0.45, x=410, command=self.joint_movj)
        
        self.frame_feed_log = Frame(
            self.root, bg="#FFFFFF", width=870, pady=10, height=400, border=2)
        # Retroalimentacion del robot 
        self.frame_feed = LabelFrame(self.frame_feed_log, text="Feedback", labelanchor="nw",
                                     bg="#FFFFFF", width=550, height=150)

        self.frame_feed.place(relx=0, rely=0, relheight=1)

        # Relación de velocidad actual
        self.set_label(self.frame_feed,
                       text="Current Speed Ratio:", rely=0.05, x=10)
        self.label_feed_speed = self.set_label(
            self.frame_feed, "", rely=0.05, x=145)
        self.set_label(self.frame_feed, text="%", rely=0.05, x=175)

        # Modo Robot
        self.set_label(self.frame_feed, text="Robot Mode:", rely=0.1, x=10)
        self.label_robot_mode = self.set_label(
            self.frame_feed, "", rely=0.1, x=95)

        # Trota y obtén coordenadas
        self.label_feed_dict = {}
        self.set_feed(LABEL_JOINT, 9, 52, 74, 117)
        self.set_feed(LABEL_COORD, 165, 209, 231, 272)

        # Digitial I/O
        self.set_label(self.frame_feed, "Digital Inputs:", rely=0.8, x=11)
        self.label_di_input = self.set_label(
            self.frame_feed, "", rely=0.8, x=100)
        self.set_label(self.frame_feed, "Digital Outputs:", rely=0.85, x=10)
        self.label_di_output = self.set_label(
            self.frame_feed, "", rely=0.85, x=100)

        # Información de error
        self.frame_err = LabelFrame(self.frame_feed, text="Error Info", labelanchor="nw",
                                    bg="#FFFFFF", width=180, height=50)
        self.frame_err.place(relx=0.65, rely=0, relheight=0.7)

        self.text_err = ScrolledText(
            self.frame_err, width=170, height=50, relief="flat")
        self.text_err.place(rely=0, relx=0, relheight=0.7, relwidth=1)

        self.set_button(self.frame_feed, "Clear", rely=0.71,
                        x=487, command=self.clear_error_info)

        # Registro
        self.frame_log = LabelFrame(self.frame_feed_log, text="Log", labelanchor="nw",
                                    bg="#FFFFFF", width=300, height=150)
        self.frame_log.place(relx=0.65, rely=0, relheight=1)

        self.text_log = ScrolledText(
            self.frame_log, width=270, height=140, relief="flat")
        self.text_log.place(rely=0, relx=0, relheight=1, relwidth=1)

        # Cliente inicial
        self.client_dash = None
        self.client_move = None
        self.client_feed = None

        self.alarm_controller_dict = self.convert_dict(alarm_controller_list)
        self.alarm_servo_dict = self.convert_dict(alarm_servo_list)

    def convert_dict(self, alarm_list):
        alarm_dict = {}
        for i in alarm_list:
            alarm_dict[i["id"]] = i
        return alarm_dict
    
    def read_file(self, path):
        with open(path, "r", encoding="utf8") as fp:
            json_data = json.load(fp)
        return json_data
    
    def mainloop(self):
        self.root.mainloop()

    def pack(self):
        self.frame_robot.pack()
        self.frame_dashboard.pack()
        self.frame_move.pack()
        self.frame_feed_log.pack()

    def set_move(self, text, label_value, default_value, entry_value, rely, master):
        self.label = Label(master, text=text)
        self.label.place(rely=rely, x=label_value)
        value = StringVar(self.root, value=default_value)
        self.entry_temp = Entry(master, width=6, textvariable=value)
        self.entry_temp.place(rely=rely, x=entry_value)
        self.entry_dict[text] = self.entry_temp

    def move_jog(self, text):
        if self.global_state["connect"]:
            self.client_move.MoveJog(text)

    def move_stop(self, event):
        if self.global_state["connect"]:
            self.client_move.MoveJog("")

    def set_button(self, master, text, rely, x, **kargs):
        self.button = Button(master, text=text, padx=5,
                             command=kargs["command"])
        self.button.place(rely=rely, x=x)

        if text != "Connect":
            self.button["state"] = "disable"
            self.button_list.append(self.button)
        return self.button
    
    def set_label(self, master, text, rely, x):
        self.label = Label(master, text=text)
        self.label.place(rely=rely, x=x)
        return self.label
    
    def connect_port(self):
        if self.global_state["connect"]:
            print("Desconexión exitosa")
            self.client_dash.close()
            self.client_feed.close()
            self.client_move.close()
            self.client_dash = None
            self.client_feed = None
            self.client_move = None

            for i in self.button_list:
                i["state"] = "disable"
            self.button_connect["text"] = "Connect"
        else:
            try:
                print("La conexión se ha realizado correctamente")
                self.client_dash = DobotApiDashboard(
                    self.entry_ip.get(), int(self.entry_dash.get()), self.text_log)
                self.client_move = DobotApiMove(
                    self.entry_ip.get(), int(self.entry_move.get()), self.text_log)
                self.client_feed = DobotApi(
                    self.entry_ip.get(), int(self.entry_feed.get()), self.text_log)
            except Exception as e:
                messagebox.showerror("Attention!", f"Connection Error:{e}")
                return
            
            for i in self.button_list:
                i["state"] = "normal"
            self.button_connect["text"] = "Disconnect"
        self.global_state["connect"] = not self.global_state["connect"]
        self.set_feed_back()

    def set_feed_back(self):
        if self.global_state["connect"]:
            thread = Thread(target=self.feed_back)
            thread.setDaemon(True)
            thread.start()