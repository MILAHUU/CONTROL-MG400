# -*- coding: utf-8 -*-
from threading import Thread
import time
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText
from dobot_api import * # type: ignore
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
    1: "INICIO_MODO_ROBOT",          
    2: "APERTURA_FRENO_MODO_ROBOT", 
    3: "",                             
    4: "MODO_ROBOT_DESACTIVADO",     
    5: "MODO_ROBOT_HABILITADO",       
    6: "RETROCESO_MODO_ROBOT",        
    7: "MODO_ROBOT_EN_EJECUCION",    
    8: "MODO_GRABACION_MODO_ROBOT",  
    9: "ERROR_MODO_ROBOT",          
    10: "PAUSA_MODO_ROBOT",          
    11: "MODO_DESPLAZAMIENTO_INCREMENTAL"  # Modo de desplazamiento incremental (Jog) del modo robot
}
