#Control de errores de los servos
alarm_servo_list = [
    {
        "id": 0,
        "level": 0,
        "en": {
            "description" : "No error",
            "cause" : "",
            "solution" : ""
        },
    },
    {
        "id": 25376,
        "level": 0,
        "en": {
            "description" : "Anomalías en los parámetros internos del servomotor",
            "cause" : "1.Caída instantánea del voltaje de la fuente de alimentación 2.Se actualizó el software 3.Falla del servodrive",
            "solution" : "System error, please contact technical support engineer"
        },
    },
    {
        "id": 21120,
        "level": 0,
        "en": {
            "description" : "Programmable logic configuration faults",
            "cause" : "1.Incompatibilidad entre las versiones del software de FPGA y MCU 2.Falla en la FPGA",
            "solution" : "System error, please contact technical support engineer"
        },
    },
    {
        "id": 29953,
        "level": 0,
        "en": {
            "description" : "FPGA software version too low",
            "cause" : "",
            "solution" : "Please contact technical support engineer"
        },
    },
    {
        "id": 29954,
        "level": 0,
        "en": {
            "description" : "Programmable logic interrupt fault",
            "cause" : "1.Falla en la FPGA 2.Anomalía en el handshake de comunicación entre FPGA y MCU 3.Tiempo de cálculo interno del controlador excedido",
            "solution" : "If connecting the power for many times, the alarm is still reported, please replace the drive"
        },
    },
    {
        "id": 25377,
        "level": 0,
        "en": {
            "description" : "Internal program exceptions",
            "cause" : "1.Falla en la EEPROM 2.Falla en el servodrive",
            "solution" : "System error, please contact technical support engineer"
        },
    },
    {
        "id": 21808,
        "level": 0,
        "en": {
            "description" : "Parameter storage failure",
            "cause" : "1.Anomalía durante la escritura de parámetros 2.Anomalía durante la lectura de parámetros",
            "solution" : "Reset the parameter and power on again, or please contact technical support engineer"
        },
    },
    {
        "id": 28962,
        "level": 0,
        "en": {
            "description" : "Product matching faults",
            "cause" : "1.El número de serie del producto (motor o controlador) no existe 2.Incompatibilidad en el nivel de potencia entre el motor y el controlador",
            "solution" : "1. Check whether the motor parameter matches the motor model in nameplate; 2.Check whether the motor and driver match, otherwise, select the right motor and driver"
        },
    },
    {
        "id": 21574,
        "level": 0,
        "en": {
            "description" : "Invalid servo ON command fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        },
    },
    {
        "id": 28964,
        "level": 0,
        "en": {
            "description" : "Absolute position mode product matching fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        },
    },
    {
        "id": 25378,
        "level": 0,
        "en": {
            "description" : "Repeated assignment of DI functions",
            "cause" : "1.Al asignar funciones DI, la misma función se asigna repetidamente a varios terminales DI 2.El número de función DI excede la cantidad de funciones DI disponibles 3.La función DI no es compatible",
            "solution" : "1. Check whether  the same function is assigned to different DI's; 2. Confirm whether the corresponding MCU supports the assigned functionality"
        },
    },
    {
        "id": 25379,
        "level": 0,
        "en": {
            "description" : "DO function allocation overrun",
            "cause" : "1.Anomalía en el controlador 2.Contacto deficiente o desconexión del cable de comunicación 3.El cable de comunicación no está conectado a tierra o la conexión a tierra es deficiente",
            "solution" : "Check whether the motor and circuit are working properly, or contact technical support engineer"
        },
    },
    {
        "id": 29488,
        "level": 0,
        "en": {
            "description" : "Data in the motor encoder ROM is incorrectly checked or parameters are not stored",
            "cause" : "",
            "solution" : "系统错误，请联系技术支持工程师"
        },
    },
    {
        "id": 8752,
        "level": 0,
        "en": {
            "description" : "Hardware overcurrent",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        },
        "zh_CN": {
            "description" : "硬件过流",
            "cause" : "1.输入指令与接通伺服同步或输入指令过快 2.制动电阻过小或短路 3.电机线缆接触不良4.电机线缆接地 5.电机UVW线缆短路 6.电机烧坏 7.增益设置不合理，电机振荡 8.编码器接线错误、老化腐蚀，编码器插头松动 9.驱动器故障",
            "solution" : "系统错误，请联系技术支持工程师"
        }
    },
    {
        "id": 8977,
        "level": 0,
        "en": {
            "description" : "DQ axis current overflow fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        },
    },
    {
        "id": 65288,
        "level": 0,
        "en": {
            "description" : "FPGA system sampling operation timeout",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        },
    },
    {
        "id": 9024,
        "level": 0,
        "en": {
            "description" : "Output shorted to ground",
            "cause" : "1.Cortocircuito a tierra en los cables de potencia del controlador (U V W) 2.Cortocircuito a tierra en el motor 3.Falla en el controlador",
            "solution" : "Please contact technical support engineer"
        },
    },
    {
        "id": 13184,
        "level": 0,
        "en": {
            "description" : "UVW phase sequence error",
            "cause" : "La secuencia de fases U V W del motor no corresponde con la de U V W del controlador",
            "solution" : "System error, please contact technical support engineer"
        },
    },
        {
        "id": 33922,
        "level": 0,
        "en": {
            "description" : "Flying Cars",
            "cause" : "",
            "solution" : "Please contact technical support engineer"
        },
        "zh_CN": {
            "description" : "飞车",
            "cause" : "1.U V W相序接线错误 2.上电时，干扰信号导致电机转子初始相位检测错误 3.编码器型号错误或接线错误 4.编码器接线松动 5.负载过大",
            "solution" : "请联系技术支持工程师"
        }
    },
    {
        "id": 12816,
        "level": 0,
        "en": {
            "description" : "Electrical over-voltage in the main circuit",
            "cause" : "1.Nivel de voltaje de entrada incorrecto 2.Falla en la resistencia de frenado 3.Resistencia de frenado demasiado grande, la velocidad de absorción de energía es demasiado lenta",
            "solution" : "System error, please contact technical support engineer"
        },
    },
        {
        "id": 12832,
        "level": 0,
        "en": {
            "description" : "Main circuit voltage undervoltage",
            "cause" : "1.Voltaje de entrada de la fuente de alimentación inestable o pérdida de energía 2.Caída de voltaje significativa durante una aceleración brusca 3.Falla en el servodrive",
            "solution" : "System error, please contact technical support engineer"
        },
    },
]