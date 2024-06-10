import os, sys
# ---------copiar estas lineas de codigo en caso de marcar error en las importaciones----------
# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Obtener la ruta del directorio del proyecto (un nivel arriba del directorio actual)
project_dir = os.path.dirname(script_dir)
# Agregar la ruta del proyecto al PYTHONPATH
sys.path.append(project_dir)
# ---------------------------------------------------------------------------------------------

import threading
from Api.dobot_api import DobotApiDashboard, DobotApi, DobotApiMove, MyType,alarmAlarmJsonFile
from time import sleep
import numpy as np
import re


# Variable global (coordenadas actuales)
current_actual = None
algorithm_queue = None
enableStatus_robot = None
robotErrorState = False
globalLockValue = threading.Lock()

def ConnectRobot():
    try:
        ip = "192.168.1.6"
        dashboardPort = 29999
        movePort = 30003
        feedPort = 30004
        print("Conectando...")
        dashboard = DobotApiDashboard(ip, dashboardPort)
        move = DobotApiMove(ip, movePort)
        feed = DobotApi(ip, feedPort)
        print(">.< Conexion exitosa >!<")
        return dashboard, move, feed
    except Exception as e:
        print(":( Error en la conexión :(")
        raise e

def RunPoint(move: DobotApiMove, point_list: list):
    move.MovL(point_list[0], point_list[1], point_list[2], point_list[3])

def GetFeed(feed: DobotApi):
    global current_actual
    global algorithm_queue
    global enableStatus_robot
    global robotErrorState
    hasRead = 0
    while True:
        data = bytes()
        while hasRead < 1440:
            temp = feed.socket_dobot.recv(1440 - hasRead)
            if len(temp) > 0:
                hasRead += len(temp)
                data += temp
        hasRead = 0
        feedInfo = np.frombuffer(data, dtype=MyType)
        if hex((feedInfo['test_value'][0])) == '0x123456789abcdef':
            globalLockValue.acquire()
            # Actualizar propiedades
            current_actual = feedInfo["tool_vector_actual"][0]
            algorithm_queue = feedInfo['isRunQueuedCmd'][0]
            enableStatus_robot=feedInfo['EnableStatus'][0]
            robotErrorState= feedInfo['ErrorStatus'][0]
            globalLockValue.release()
        sleep(0.001)

def WaitArrive(point_list):
    while True:
        is_arrive = True
        globalLockValue.acquire()
        if current_actual is not None:
            for index in range(4):
                if (abs(current_actual[index] - point_list[index]) > 1):
                    is_arrive = False
            if is_arrive :
                globalLockValue.release()
                return
        globalLockValue.release()  
        sleep(0.001)

def ClearRobotError(dashboard: DobotApiDashboard):
    global robotErrorState
    dataController,dataServo =alarmAlarmJsonFile()    # Leer el código de alarma del controlador y el servo
    while True:
      globalLockValue.acquire()
      if robotErrorState:
                numbers = re.findall(r'-?\d+', dashboard.GetErrorID())
                numbers= [int(num) for num in numbers]
                if (numbers[0] == 0):
                  if (len(numbers)>1):
                    for i in numbers[1:]:
                      alarmState=False
                      if i==-2:
                          print("Alerta de la máquina en Colisión",i)
                          alarmState=True
                      if alarmState:
                          continue                
                      for item in dataController:
                        if  i==item["id"]:
                            print("Alarma de máquina Controller errorid",i,item["zh_CN"]["description"])
                            alarmState=True
                            break 
                      if alarmState:
                          continue
                      for item in dataServo:
                        if  i==item["id"]:
                            print("Alarma de máquina Servo errorid",i,item["zh_CN"]["description"])
                            break  
                       
                    choose = input("Introduzca 1, el error se borrará y la máquina seguirá funcionando: ")     
                    if  int(choose)==1:
                        dashboard.ClearError()
                        sleep(0.01)
                        dashboard.Continue()

      else:  
         if int(enableStatus_robot[0])==1 and int(algorithm_queue[0])==0:
            dashboard.Continue()
      globalLockValue.release()
      sleep(5)
       
if __name__ == '__main__':
    dashboard, move, feed = ConnectRobot()
    print("Comience a habilitar...")
    dashboard.EnableRobot()
    print("Habilitación completa:)")
    feed_thread = threading.Thread(target=GetFeed, args=(feed,))
    feed_thread.setDaemon(True)
    feed_thread.start()
    feed_thread1 = threading.Thread(target=ClearRobotError, args=(dashboard,))
    feed_thread1.setDaemon(True)
    feed_thread1.start()
    print("Ejecución de bucles...")
  
  # Definición de nuevos puntos de movimiento
    point_a = [100, 280, -60, 200]
    point_b = [260, 100, -30, 170]
    point_c = [220, 260, -60, 150]
    point_d = [250, 280, -40, 180]
    point_e = [200, 100, -70, 130]

    # Nuevos puntos de movimiento adicionales
    point_f = [150, 150, -50, 160]
    point_g = [180, 220, -60, 140]
    point_h = [120, 180, -70, 110]
    point_i = [140, 240, -55, 190]
    point_j = [170, 130, -45, 120]
    
    # Lista de puntos a los que se moverá el robot
    points = [point_a, point_b, point_c, point_d, point_e, point_f, point_g, point_h, point_i, point_j]
    
    while True:
        for point in points:
            RunPoint(move, point)
            WaitArrive(point)
