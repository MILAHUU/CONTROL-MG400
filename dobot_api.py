import socket
import threading
from tkinter import Text, END
import datetime
import numpy as np
import os
import json

alarmControllerFile="files/alarm_controller.json"
alarmServoFile="files/alarm_servo.json"

# Port Feedback
MyType=np.dtype([('len', np.int16, ), 
                ('Reserve', np.int16, (3,) ),
                ('digital_input_bits', np.int64, ), 
                ('digital_outputs', np.int64, ), 
                ('robot_mode', np.int64, ), 
                ('controller_timer', np.int64, ),
                ('run_time', np.int64, ), 
                ('test_value', np.int64, ), 
                ('safety_mode', np.float64, ), 
                ('speed_scaling', np.float64, ), 
                ('linear_momentum_norm', np.float64, ),
                ('v_main', np.float64, ), 
                ('v_robot', np.float64, ), 
                ('i_robot', np.float64, ), 
                ('program_state', np.float64, ), 
                ('safety_status', np.float64, ), 
                ('tool_accelerometer_values', np.float64, (3,)), 
                ('elbow_position', np.float64, (3,)), 
                ('elbow_velocity', np.float64, (3,)), 
                ('q_target', np.float64, (6,)), 
                ('qd_target', np.float64,(6,)),
                ('qdd_target', np.float64, (6,)), 
                ('i_target', np.float64,(6,)), 
                ('m_target', np.float64, (6,)), 
                ('q_actual', np.float64, (6,)), 
                ('qd_actual', np.float64, (6,)), 
                ('i_actual', np.float64, (6,)), 
                ('i_control', np.float64, (6,)), 
                ('tool_vector_actual', np.float64, (6,)), 
                ('TCP_speed_actual', np.float64, (6,)), 
                ('TCP_force', np.float64, (6,)),
                ('Tool_vector_target', np.float64, (6,)), 
                ('TCP_speed_target', np.float64, (6,)), 
                ('motor_temperatures', np.float64, (6,)), 
                ('joint_modes', np.float64, (6,)), 
                ('v_actual', np.float64, (6,)), 
                ('handtype', np.int8, (4,)),
                ('userCoordinate', np.int8, (1,)), 
                ('toolCoordinate', np.int8, (1,)),
                ('isRunQueuedCmd', np.int8, (1,)), 
                ('isPauseCmdFlag', np.int8, (1,)),
                ('velocityRatio', np.int8, (1,)), 
                ('accelerationRatio', np.int8, (1,)),
                ('jerkRatio', np.int8, (1,)), 
                ('xyzVelocityRatio', np.int8, (1,)),
                ('rVelocityRatio', np.int8, (1,)), 
                ('xyzAccelerationRatio', np.int8, (1,)),
                ('rAccelerationRatio', np.int8, (1,)), 
                ('xyzJerkRatio', np.int8, (1,)),
                ('rJerkRatio', np.int8, (1,)), 
                ('BrakeStatus', np.int8, (1,)),
                ('EnableStatus', np.int8, (1,)),
                ('DragStatus', np.int8, (1,)),
                ('RunningStatus', np.int8, (1,)),
                ('ErrorStatus', np.int8, (1,)),
                ('JogStatus', np.int8, (1,)),
                ('RobotType', np.int8, (1,)),
                ('DragButtonSignal', np.int8, (1,)),
                ('EnableButtonSignal', np.int8, (1,)),
                ('RecordButtonSignal', np.int8, (1,)),
                ('ReappearButtonSignal', np.int8, (1,)),
                ('JawButtonSignal', np.int8, (1,)),
                ('SixForceOnline', np.int8, (1,)),#1037
                ('Reserve2', np.int8, (82,)),
                ('m_actual[6]', np.float64, (6,)), 
                ('load', np.float64, (1,)),
                ('centerX', np.float64, (1,)), 
                ('centerY', np.float64, (1,)),
                ('centerZ', np.float64, (1,)), 
                ('user', np.float64, (6,)),
                ('tool', np.float64, (6,)), 
                ('traceIndex', np.int64,),
                ('SixForceValue', np.int64, (6,)),
                ('TargetQuaternion', np.float64, (4,)),
                ('ActualQuaternion', np.float64, (4,)),
                ('Reserve3', np.int8, (24,)),
                ])

#Lectura de archivos de controlador y servoalarma
def alarmAlarmJsonFile():
    currrntDirectory=os.path.dirname(__file__)
    jsonContrellorPath=os.path.join(currrntDirectory,alarmControllerFile)
    jsonServoPath=os.path.join(currrntDirectory,alarmServoFile)
    
    with open(jsonContrellorPath,encoding='utf-8') as f:
        dataController=json.load(f)
    with open(jsonServoPath,encoding='utf-8') as f:
        dataServo=json.load(f)
    return dataController,dataServo   
 

class DobotApi:
    def __init__(self, ip, port, *args):
        self.ip = ip
        self.port = port
        self.socket_dobot = 0
        self.__globalLock = threading.Lock()
        self.text_log: Text = None
        if args:
            self.text_log = args[0]

        if self.port == 29999 or self.port == 30003 or self.port == 30004:
            try:
                self.socket_dobot = socket.socket()
                self.socket_dobot.connect((self.ip, self.port))
            except socket.error:
                print(socket.error)
                raise Exception(
                    f"No se puede configurar el puerto de uso de la conexión de socket {self.port} !", socket.error)
        else:
            raise Exception(
                f"La conexión al servidor del panel de control necesita usar el puerto {self.port} !")

    def log(self, text):
        if self.text_log:
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            self.text_log.insert(END, date+text+"\n")
        else:
            print(text)

    def send_data(self, string):
        try:
            self.log(f"Send to {self.ip}:{self.port}: {string}")
            self.socket_dobot.send(str.encode(string, 'utf-8'))
        except Exception as e:
            print(e)

    def wait_reply(self):
        """
        Leer el valor devuelto
        """
        data = ""
        try:
            data = self.socket_dobot.recv(1024)
        except Exception as e:
            print(e)

        finally:
            if len(data) == 0:
                data_str = data
            else:
                data_str = str(data, encoding="utf-8")
                self.log(f'Receive from {self.ip}:{self.port}: {data_str}')
            return data_str 

    def close(self):
        """
        Cierra el puerto
        """
        if (self.socket_dobot != 0):
            self.socket_dobot.close()

    def sendRecvMsg(self, string):
        """
        envia-recv y sincronizacion
        """
        with self.__globalLock:
            self.send_data(string)
            recvData = self.wait_reply()
            return recvData

    def __del__(self):
        self.close()


class DobotApiDashboard(DobotApi):
    """
    Define el dobot_api_dashboard de clase para establecer una conexión con Dobot
    """

    def EnableRobot(self,*dynParams):
        """
        Habilitar el robot
        """
        string = "EnableRobot("
        for i in range(len(dynParams)):
         if i == len(dynParams)-1:
            string = string + str(dynParams[i])
         else:
            string = string + str(dynParams[i]) + ","
        string = string + ")"
        return self.sendRecvMsg(string)

    def DisableRobot(self):
        """
        Desabilita el robot
        """
        string = "DisableRobot()"
        return self.sendRecvMsg(string)

    def ClearError(self):
        """
        Borrar la información de alarma del controlador
        """
        string = "ClearError()"
        return self.sendRecvMsg(string)

    def ResetRobot(self):
        """
        Detiene el robot
        """
        string = "ResetRobot()"
        return self.sendRecvMsg(string)

    def SpeedFactor(self, speed):
        """
        Establecer la tarifa global   
        velocidad:valor de la tasa(Rango de valores:1~100)
        """
        string = "SpeedFactor({:d})".format(speed)
        return self.sendRecvMsg(string)

    def User(self, index):
        """
        Seleccionar el índice del sistema de coordenadas del usuario calibrado:
        Índice calibrado de las coordenadas del usuario
        """
        string = "User({:d})".format(index)
        return self.sendRecvMsg(string)

    def Tool(self, index):
        """
        Seleccionar el índice del sistema de coordenadas de la herramienta calibrada:
        Índice calibrado de las coordenadas de la herramienta
        """
        string = "Tool({:d})".format(index)
        return self.sendRecvMsg(string)

    def RobotMode(self):
        """
        Ver el estado del robot
        """
        string = "RobotMode()"
        return self.sendRecvMsg(string)

    def PayLoad(self, weight, inertia):
        """
        Ajuste de la carga del robot:
        peso: El peso de la carga
        inercia: El momento de inercia de la carga
        """
        string = "PayLoad({:f},{:f})".format(weight, inertia)
        return self.sendRecvMsg(string)

    def DO(self, index, status):
        """
        Establecer la salida de señal digital (Instrucción en cola):
        índice: Índice de salida digital (Rango de valores: 1~24)
        estado: Estado del puerto de salida de señal digital (0: Nivel bajo, 1: Nivel alto
        """
        string = "DO({:d},{:d})".format(index, status)
        return self.sendRecvMsg(string)

    def AccJ(self, speed):
        """
        Establecer la relación de aceleración de la articulación (Solo para los comandos MovJ, MovJIO, MovJR, JointMovJ):
        velocidad: Relación de aceleración de la articulación (Rango de valores: 1~100)
        """
        string = "AccJ({:d})".format(speed)
        return self.sendRecvMsg(string)

    def AccL(self, speed):
        """
        Establecer la relación de aceleración del sistema de coordenadas (Solo para los comandos MovL, MovLIO, MovLR, Jump, Arc, Circle):
        velocidad: Relación de aceleración cartesiana (Rango de valores: 1~100)
        """
        string = "AccL({:d})".format(speed)
        return self.sendRecvMsg(string)

    def SpeedJ(self, speed):
        """
        Establecer la relación de velocidad de la articulación (Solo para los comandos MovJ, MovJIO, MovJR, JointMovJ):
        velocidad: Relación de velocidad de la articulación (Rango de valores: 1~100)
        """
        string = "SpeedJ({:d})".format(speed)
        return self.sendRecvMsg(string)

    def SpeedL(self, speed):
        """
        Establecer la relación de aceleración cartesiana (Solo para los comandos MovL, MovLIO, MovLR, Jump, Arc, Circle):
        velocidad: Relación de aceleración cartesiana (Rango de valores: 1~100)
        """
        string = "SpeedL({:d})".format(speed)
        return self.sendRecvMsg(string)

    def Arch(self, index):
        """
        Establecer el índice de parámetro de la compuerta de salto (Este índice contiene: 
        altura de elevación del punto de inicio, altura máxima de elevación, altura de descenso del punto final)
        índice: Índice del parámetro (Rango de valores: 0~9)
        """
        string = "Arch({:d})".format(index)
        return self.sendRecvMsg(string)

    def CP(self, ratio):
        """
        Establecer la relación de transición suave
        ratio : Relación de transición suave (Rango de valores: 1~100)
        """
        string = "CP({:d})".format(ratio)
        return self.sendRecvMsg(string)

    def LimZ(self, value):
        """
        Establecer la altura máxima de elevación de los parámetros de tipo de puerta
        valor : Altura máxima de elevación (Altamente restringido: No exceder la posición límite del eje Z del manipulador)
        """
        string = "LimZ({:d})".format(value)
        return self.sendRecvMsg(string)

    def RunScript(self, project_name):
        """
        Ejecutar el archivo de script
        nombre_del_proyecto: Nombre del archivo de script
        """
        string = "RunScript({:s})".format(project_name)
        return self.sendRecvMsg(string)

    def StopScript(self):
        """
        Detener scripts
        """
        string = "StopScript()"
        return self.sendRecvMsg(string)

    def PauseScript(self):
        """
        Pausa del scrpit
        """
        string = "PauseScript()"
        return self.sendRecvMsg(string)

    def ContinueScript(self):
        """
        Continuar ejecutando el scrpit
        """
        string = "ContinueScript()"
        return self.sendRecvMsg(string)

    def GetHoldRegs(self, id, addr, count, type=None):
        """
        Leer registro de retención
        id: NÚMERO del dispositivo secundario (Se pueden admitir hasta cinco dispositivos. El valor varía de 0 a 4.
        Se establece en 0 al acceder al esclavo interno del controlador)
        addr: Dirección de inicio de retención del registro (Rango de valores: 30954095)
        count: Lee el número especificado de tipos de datos (Rango de valores: 116)
        type: El tipo de datos
        Si es nulo, se lee el entero sin signo de 16 bits (2 bytes, ocupando 1 registro) de forma predeterminada
        "U16": lee enteros sin signo de 16 bits (2 bytes, ocupando 1 registro)
        "U32": lee enteros sin signo de 32 bits (4 bytes, ocupando 2 registros)
        "F32": lee número de punto flotante de precisión simple de 32 bits (4 bytes, ocupando 2 registros)
        "F64": lee número de punto flotante de doble precisión de 64 bits (8 bytes, ocupando 4 registros)
        """
        if type is not None:  
          string = "GetHoldRegs({:d},{:d},{:d},{:s})".format(
            id, addr, count, type)
        else:
          string = "GetHoldRegs({:d},{:d},{:d})".format(
            id, addr, count)   
        return self.sendRecvMsg(string)

    def SetHoldRegs(self, id, addr, count, table, type=None):
        """
        Escribir registro de retención
        id: NÚMERO del dispositivo secundario (Se pueden admitir hasta cinco dispositivos. El valor varía de 0 a 4.
        Se establece en 0 al acceder al esclavo interno del controlador)
        addr: Dirección de inicio de retención del registro (Rango de valores: 30954095)
        count: Escribe el número especificado de tipos de datos (Rango de valores: 116)
        type: El tipo de datos
        Si es nulo, se escribe el entero sin signo de 16 bits (2 bytes, ocupando 1 registro) de forma predeterminada
        "U16": escribe enteros sin signo de 16 bits (2 bytes, ocupando 1 registro)
        "U32": escribe enteros sin signo de 32 bits (4 bytes, ocupando 2 registros)
        "F32": escribe número de punto flotante de precisión simple de 32 bits (4 bytes, ocupando 2 registros)
        "F64": escribe número de punto flotante de doble precisión de 64 bits (8 bytes, ocupando 4 registros)
        """
        if type is not None:
         string = "SetHoldRegs({:d},{:d},{:d},{:d})".format(
            id, addr, count, table)
        else:
         string = "SetHoldRegs({:d},{:d},{:d},{:d},{:s})".format(
            id, addr, count, table, type)
        return self.sendRecvMsg(string)

    def GetErrorID(self):
        """
        Obtener el código de error del robot
        """
        string = "GetErrorID()"
        return self.sendRecvMsg(string)
    
    
    def DOExecute(self,offset1,offset2):
        string = "DOExecute({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)
      
    def ToolDO(self,offset1,offset2):
        string = "ToolDO({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)

    def ToolDOExecute(self,offset1,offset2):
        string = "ToolDOExecute({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)

    def  SetArmOrientation(self,offset1):
        string = "SetArmOrientation({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)

    def SetPayload(self, offset1, *dynParams):
        string = "SetPayload({:f}".format(
            offset1)
        for params in dynParams:
          string = string +","+ str(params)+","
        string = string + ")"
        return self.sendRecvMsg(string)

    def PositiveSolution(self,offset1,offset2,offset3,offset4,user,tool):   
        string = "PositiveSolution({:f},{:f},{:f},{:f},{:d},{:d}".format(offset1,offset2,offset3,offset4,user,tool)+")"
        return self.sendRecvMsg(string)

    def InverseSolution(self,offset1,offset2,offset3,offset4,user,tool,*dynParams):       
        string = "InverseSolution({:f},{:f},{:f},{:f},{:d},{:d}".format(offset1,offset2,offset3,offset4,user,tool)
        for params in dynParams:
            print(type(params), params)
            string = string + repr(params)
        string = string + ")"
        return self.sendRecvMsg(string)     

    def SetCollisionLevel(self,offset1):
        string = "SetCollisionLevel({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)

    def  GetAngle(self):
        string = "GetAngle()"
        return self.sendRecvMsg(string)

    def  GetPose(self):   
        string = "GetPose()"
        return self.sendRecvMsg(string)
    
    def EmergencyStop(self):
        string = "EmergencyStop()"
        return self.sendRecvMsg(string)


    def ModbusCreate(self,ip,port,slave_id,isRTU):
        string ="ModbusCreate({:s},{:d},{:d},{:d}".format(ip,port,slave_id,isRTU)+")"
        return self.sendRecvMsg(string)
    
    def ModbusClose(self,offset1):
        string = "ModbusClose({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)

    def GetInBits(self,offset1,offset2,offset3):
        string = "GetInBits({:d},{:d},{:d}".format(offset1,offset2,offset3)+")"
        return self.sendRecvMsg(string)        

    def GetInRegs(self,offset1,offset2,offset3,*dynParams):
        string = "GetInRegs({:d},{:d},{:d}".format(offset1,offset2,offset3)
        for params in dynParams:
            print(type(params), params)
            string = string + params[0]
        string = string + ")"
        return self.sendRecvMsg(string)  

    def GetCoils(self,offset1,offset2,offset3):
        string = "GetCoils({:d},{:d},{:d}".format(offset1,offset2,offset3)+")"
        return self.sendRecvMsg(string)          

    def SetCoils(self,offset1,offset2,offset3,offset4):
        string = "SetCoils({:d},{:d},{:d}".format(offset1,offset2,offset3)+","+ repr(offset4)+")"
        print(str(offset4))
        return self.sendRecvMsg(string)              

    def DI(self,offset1):
        string = "DI({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)        

    def ToolDI(self,offset1):
        string = "DI({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)   

    def DOGroup(self,*dynParams):
        string = "DOGroup("
        for params in dynParams:
            string = string + str(params)+","
        string =string+ ")"   
        return self.wait_reply()  

    def BrakeControl(self,offset1,offset2): 
        string = "BrakeControl({:d},{:d}".format(offset1,offset2)+")"
        return self.sendRecvMsg(string)             

    def StartDrag(self):
        string = "StartDrag()"
        return self.sendRecvMsg(string)      

    def StopDrag(self):
        string = "StopDrag()"
        return self.sendRecvMsg(string)           

    def LoadSwitch(self,offset1):    
        string = "LoadSwitch({:d}".format(offset1)+")"
        return self.sendRecvMsg(string)                                                       

    def wait(self):
        string = "wait()"
        return self.sendRecvMsg(string)

    def pause(self):
        string = "pause()"
        return self.sendRecvMsg(string)

    def Continue(self):
        string = "continue()"
        return self.sendRecvMsg(string)
    
class DobotApiMove(DobotApi):
    """
    Define la clase dobot_api_move para establecer una conexión con Dobot
    """

    def MovJ(self, x, y, z, r,*dynParams):
        """
        Interfaz de movimiento de articulaciones (modo de movimiento punto a punto)
        x: Un número en el sistema de coordenadas cartesianas x
        y: Un número en el sistema de coordenadas cartesianas y
        z: Un número en el sistema de coordenadas cartesianas z
        r: Un número en el sistema de coordenadas cartesianas R
        """
        string = "MovJ({:f},{:f},{:f},{:f}".format(
            x, y, z, r)
        for params in dynParams:
             string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)  
        return self.sendRecvMsg(string)

    def MovL(self, x, y, z, r,*dynParams):
        """
        Interfaz de movimiento del sistema de coordenadas (modo de movimiento lineal)
        x: Un número en el sistema de coordenadas cartesianas x
        y: Un número en el sistema de coordenadas cartesianas y
        z: Un número en el sistema de coordenadas cartesianas z
        r: Un número en el sistema de coordenadas cartesianas R
        """
        string = "MovL({:f},{:f},{:f},{:f}".format(
            x, y, z, r)
        for params in dynParams:
             string =string+ ","+ str(params)
        string =string+ ")" 
        print(string) 
        return self.sendRecvMsg(string)

    def JointMovJ(self, j1, j2, j3, j4,*dynParams):
        """
        Interfaz de movimiento de articulaciones (modo de movimiento lineal)
        j1~j6: Valores de posición del punto en cada articulación
        """
        string = "JointMovJ({:f},{:f},{:f},{:f}".format(
            j1, j2, j3, j4)
        for params in dynParams:
            string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)
        return self.sendRecvMsg(string)

    def Jump(self):
        print("待定")

    def RelMovJ(self, x, y, z, r,*dynParams):
        """
        Interfaz de movimiento de desplazamiento (modo de movimiento punto a punto)
        j1~j6: Valores de posición del punto en cada articulación
        """
        string = "RelMovJ({:f},{:f},{:f},{:f}".format(
            x, y, z, r)
        for params in dynParams:
            string =string+ ","+ str(params)
        string =string+ ")" 
        return self.sendRecvMsg(string)

    def RelMovL(self, offsetX, offsetY, offsetZ,offsetR,*dynParams):
        """
        Interfaz de movimiento de desplazamiento (modo de movimiento punto a punto)
        x: Desplazamiento en el sistema de coordenadas cartesianas x
        y: Desplazamiento en el sistema de coordenadas cartesianas y
        z: Desplazamiento en el sistema de coordenadas cartesianas Z
        r: Desplazamiento en el sistema de coordenadas cartesianas R
        """
        string = "RelMovL({:f},{:f},{:f},{:f}".format(offsetX, offsetY, offsetZ,offsetR)
        for params in dynParams:
            string =string+ ","+ str(params)
        string =string+ ")" 
        return self.sendRecvMsg(string)

    def MovLIO(self, x, y, z, r, *dynParams):
        """
       Establecer el estado del puerto de salida digital en paralelo mientras se mueve en línea recta
        x: Un número en el sistema de coordenadas cartesianas x
        y: Un número en el sistema de coordenadas cartesianas y
        z: Un número en el sistema de coordenadas cartesianas z
        r: Un número en el sistema de coordenadas cartesianas r
        *dynParams: Configuraciones de parámetros (Modo, Distancia, Índice, Estado)
        Modo: Establecer el modo de distancia (0: Porcentaje de distancia; 1: Distancia desde el punto de inicio o el punto de destino)
        Distancia: Ejecuta la distancia especificada (Si el Modo es 0, el valor varía de 0 a 100; Cuando el Modo es 1, si el valor es positivo,
        indica la distancia desde el punto de inicio. Si el valor de Distancia es negativo, representa la distancia desde el punto de destino)
        Índice: Índice de salida digital (Rango de valores: 1~24)
        Estado: Estado de salida digital (Rango de valores: 0/1)
        """
        # example： MovLIO(0,50,0,0,0,0,(0,50,1,0),(1,1,2,1))
        string = "MovLIO({:f},{:f},{:f},{:f}".format(
            x, y, z, r)
        for params in dynParams:
            string =string+ ","+ str(params)
        string =string+ ")" 
        return self.sendRecvMsg(string)

    def MovJIO(self, x, y, z, r, *dynParams):
        """
        Set the digital output port state in parallel during point-to-point motion
        x: A number in the Cartesian coordinate system x
        y: A number in the Cartesian coordinate system y
        z: A number in the Cartesian coordinate system z
        r: A number in the Cartesian coordinate system r
        *dynParams :Parameter Settings（Mode、Distance、Index、Status)
                    Mode :Set Distance mode (0: Distance percentage; 1: distance from starting point or target point)
                    Distance :Runs the specified distance（If Mode is 0, the value ranges from 0 to 100；When Mode is 1, if the value is positive,
                             it indicates the distance from the starting point. If the value of Distance is negative, it represents the Distance from the target point）
                    Index ：Digital output index （Value range：1~24）
                    Status ：Digital output state（Value range：0/1）
        """
        # example： MovJIO(0,50,0,0,0,0,(0,50,1,0),(1,1,2,1))
        string = "MovJIO({:f},{:f},{:f},{:f}".format(
            x, y, z, r)
        self.log("Send to 192.168.1.6:29999:" + string)
        for params in dynParams:
            string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)
        return self.sendRecvMsg(string)

    def Arc(self, x1, y1, z1, r1, x2, y2, z2, r2,*dynParams):
        """
        Circular motion instruction
        x1, y1, z1, r1 :Is the point value of intermediate point coordinates
        x2, y2, z2, r2 :Is the value of the end point coordinates
        Note: This instruction should be used together with other movement instructions
        """
        string = "Arc({:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f}".format(
            x1, y1, z1, r1, x2, y2, z2, r2)
        for params in dynParams:
            string =string+ ","+ str(params)
        string =string+ ")" 
        print(string)
        return self.sendRecvMsg(string)

    def Circle(self, x1, y1, z1, r1, x2, y2, z2, r2,count,*dynParams):
        """
        Full circle motion command
        count：Run laps
        x1, y1, z1, r1 :Is the point value of intermediate point coordinates
        x2, y2, z2, r2 :Is the value of the end point coordinates
        Note: This instruction should be used together with other movement instructions
        """
        string = "Circle({:f},{:f},{:f},{:f},{:f},{:f},{:f},{:f},{:d}".format(
             x1, y1, z1, r1, x2, y2, z2, r2, count)
        for params in dynParams:
            string = string + ","+ str(params)
        string = string + ")" 
        return self.sendRecvMsg(string)

    def MoveJog(self, axis_id=None, *dynParams):
        """
        Joint motion
        axis_id: Joint motion axis, optional string value:
            J1+ J2+ J3+ J4+ J5+ J6+
            J1- J2- J3- J4- J5- J6- 
            X+ Y+ Z+ Rx+ Ry+ Rz+ 
            X- Y- Z- Rx- Ry- Rz-
        *dynParams: Parameter Settings（coord_type, user_index, tool_index）
                    coord_type: 1: User coordinate 2: tool coordinate (default value is 1)
                    user_index: user index is 0 ~ 9 (default value is 0)
                    tool_index: tool index is 0 ~ 9 (default value is 0)
        """
        if axis_id is not None:
          string = "MoveJog({:s}".format(axis_id)
        else:
          string = "MoveJog("
        for params in dynParams:
            string = string + ","+ str(params)
        string = string + ")" 
        return self.sendRecvMsg(string)


    def Sync(self):
        """
        The blocking program executes the queue instruction and returns after all the queue instructions are executed
        """
        string = "Sync()"
        return self.sendRecvMsg(string)

    def RelMovJUser(self, offset_x, offset_y, offset_z, offset_r, user, *dynParams):
        """
        The relative motion command is carried out along the user coordinate system, and the end motion mode is joint motion
        offset_x: X-axis direction offset
        offset_y: Y-axis direction offset
        offset_z: Z-axis direction offset
        offset_r: R-axis direction offset

        user: Select the calibrated user coordinate system, value range: 0 ~ 9
        *dynParams: parameter Settings（speed_j, acc_j, tool）
                    speed_j: Set joint speed scale, value range: 1 ~ 100
                    acc_j: Set acceleration scale value, value range: 1 ~ 100
                    tool: Set tool coordinate system index
        """
        string = "RelMovJUser({:f},{:f},{:f},{:f}, {:d}".format(
            offset_x, offset_y, offset_z, offset_r, user)
        for params in dynParams:
            string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)

    def RelMovLUser(self, offset_x, offset_y, offset_z, offset_r, user, *dynParams):
        """
        The relative motion command is carried out along the user coordinate system, and the end motion mode is linear motion
        offset_x: X-axis direction offset
        offset_y: Y-axis direction offset
        offset_z: Z-axis direction offset
        offset_r: R-axis direction offset
        user: Select the calibrated user coordinate system, value range: 0 ~ 9
        *dynParams: parameter Settings（speed_l, acc_l, tool）
                    speed_l: Set Cartesian speed scale, value range: 1 ~ 100
                    acc_l: Set acceleration scale value, value range: 1 ~ 100
                    tool: Set tool coordinate system index
        """
        string = "RelMovLUser({:f},{:f},{:f},{:f}, {:d}".format(
            offset_x, offset_y, offset_z, offset_r, user)
        for params in dynParams:
            string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)

    def RelJointMovJ(self, offset1, offset2, offset3, offset4, *dynParams):
        """
        The relative motion command is carried out along the joint coordinate system of each axis, and the end motion mode is joint motion
        Offset motion interface (point-to-point motion mode)
        j1~j6:Point position values on each joint
        *dynParams: parameter Settings（speed_j, acc_j, user）
                    speed_j: Set Cartesian speed scale, value range: 1 ~ 100
                    acc_j: Set acceleration scale value, value range: 1 ~ 100
        """
        string = "RelJointMovJ({:f},{:f},{:f},{:f}".format(
            offset1, offset2, offset3, offset4)
        for params in dynParams:
           string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)
    
    def MovJExt(self, offset1, *dynParams):
        string = "MovJExt({:f}".format(
            offset1)
        for params in dynParams:
           string = string + ","+ str(params)
        string = string + ")"
        return self.sendRecvMsg(string)

    def SyncAll(self):
        string = "SyncAll()"
        return self.sendRecvMsg(string)

    
