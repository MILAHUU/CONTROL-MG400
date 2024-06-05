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