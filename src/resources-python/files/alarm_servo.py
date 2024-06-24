#Control de errores de los servos
alarm_servo_list = [
    {
        "id": 0,
        "level": 0,
        "en": {
            "description" : "No error",
            "cause" : "",
            "solution" : ""
        }
    },
    {
        "id": 25376,
        "level": 0,
        "en": {
            "description" : "Anomalías en los parámetros internos del servomotor",
            "cause" : "1.Caída instantánea del voltaje de la fuente de alimentación 2.Se actualizó el software 3.Falla del servodrive",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 21120,
        "level": 0,
        "en": {
            "description" : "Programmable logic configuration faults",
            "cause" : "1.Incompatibilidad entre las versiones del software de FPGA y MCU 2.Falla en la FPGA",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 29953,
        "level": 0,
        "en": {
            "description" : "FPGA software version too low",
            "cause" : "",
            "solution" : "Please contact technical support engineer"
        }
    },
    {
        "id": 29954,
        "level": 0,
        "en": {
            "description" : "Programmable logic interrupt fault",
            "cause" : "1.Falla en la FPGA 2.Anomalía en el handshake de comunicación entre FPGA y MCU 3.Tiempo de cálculo interno del controlador excedido",
            "solution" : "If connecting the power for many times, the alarm is still reported, please replace the drive"
        }
    },
    {
        "id": 25377,
        "level": 0,
        "en": {
            "description" : "Internal program exceptions",
            "cause" : "1.Falla en la EEPROM 2.Falla en el servodrive",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 21808,
        "level": 0,
        "en": {
            "description" : "Parameter storage failure",
            "cause" : "1.Anomalía durante la escritura de parámetros 2.Anomalía durante la lectura de parámetros",
            "solution" : "Reset the parameter and power on again, or please contact technical support engineer"
        }
    },
    {
        "id": 28962,
        "level": 0,
        "en": {
            "description" : "Product matching faults",
            "cause" : "1.El número de serie del producto (motor o controlador) no existe 2.Incompatibilidad en el nivel de potencia entre el motor y el controlador",
            "solution" : "1. Check whether the motor parameter matches the motor model in nameplate; 2.Check whether the motor and driver match, otherwise, select the right motor and driver"
        }
    },
    {
        "id": 21574,
        "level": 0,
        "en": {
            "description" : "Invalid servo ON command fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 28964,
        "level": 0,
        "en": {
            "description" : "Absolute position mode product matching fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 25378,
        "level": 0,
        "en": {
            "description" : "Repeated assignment of DI functions",
            "cause" : "1.Al asignar funciones DI, la misma función se asigna repetidamente a varios terminales DI 2.El número de función DI excede la cantidad de funciones DI disponibles 3.La función DI no es compatible",
            "solution" : "1. Check whether  the same function is assigned to different DI's; 2. Confirm whether the corresponding MCU supports the assigned functionality"
        }
    },
    {
        "id": 25379,
        "level": 0,
        "en": {
            "description" : "DO function allocation overrun",
            "cause" : "1.Anomalía en el controlador 2.Contacto deficiente o desconexión del cable de comunicación 3.El cable de comunicación no está conectado a tierra o la conexión a tierra es deficiente",
            "solution" : "Check whether the motor and circuit are working properly, or contact technical support engineer"
        }
    },
    {
        "id": 29488,
        "level": 0,
        "en": {
            "description" : "Data in the motor encoder ROM is incorrectly checked or parameters are not stored",
            "cause" : "",
            "solution" : "Error del sistema, póngase en contacto con el ingeniero de soporte técnico"
        }
    },
    {
        "id": 8752,
        "level": 0,
        "en": {
            "description" : "Hardware overcurrent",
            "cause" : "1. El comando de entrada está sincronizado con el servo de encendido y encendido o el comando de entrada es demasiado rápido 2. La resistencia de frenado es demasiado pequeña o está en cortocircuito 3. El cable del motor no está en buen contacto 4. El cable del motor está conectado a tierra 5. El cable UVW del motor está en cortocircuito 6. El motor está quemado 7. El ajuste de ganancia no es razonable y el motor oscila 8. El codificador está cableado incorrectamente, envejecido y corrosión, y el enchufe del codificador está suelto 9. El controlador está defectuoso",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 8977,
        "level": 0,
        "en": {
            "description" : "DQ axis current overflow fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 65288,
        "level": 0,
        "en": {
            "description" : "FPGA system sampling operation timeout",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 9024,
        "level": 0,
        "en": {
            "description" : "Output shorted to ground",
            "cause" : "1.Cortocircuito a tierra en los cables de potencia del controlador (U V W) 2.Cortocircuito a tierra en el motor 3.Falla en el controlador",
            "solution" : "Please contact technical support engineer"
        }
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
            "cause" : "1. Error de cableado de secuencia de fase U V W 2. Al encender, la señal de interferencia causa el error de detección de fase inicial del rotor del motor 3. El modelo del codificador es incorrecto o un error de cableado 4. El cableado del codificador está suelto 5. La carga es demasiado grande",
            "solution" : "Please contact technical support engineer"
        }
    },
    {
        "id": 12816,
        "level": 0,
        "en": {
            "description" : "Electrical over-voltage in the main circuit",
            "cause" : "1.Nivel de voltaje de entrada incorrecto 2.Falla en la resistencia de frenado 3.Resistencia de frenado demasiado grande, la velocidad de absorción de energía es demasiado lenta",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 12832,
        "level": 0,
        "en": {
            "description" : "Main circuit voltage undervoltage",
            "cause" : "1.Voltaje de entrada de la fuente de alimentación inestable o pérdida de energía 2.Caída de voltaje significativa durante una aceleración brusca 3.Falla en el servodrive",
            "solution" : "System error, please contact technical support engineer"
        }
    },
     {
        "id": 12592,
        "level": 0,
        "en": {
            "description" : "Main circuit electrical shortage",
            "cause" : "1. Potencia de entrada R S T Faltan 2 fases 2. La unidad está dañada",
            "solution" : "Check the cable connection of power, otherwise, replace the driver"
        }
    },
        {
        "id": 12576,
        "level": 0,
        "en": {
            "description" : "Control of electrical undervoltage",
            "cause" : "1. La fuente de alimentación de control es inestable o está apagada; 2. El cable de control está en mal contacto",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 33920,
        "level": 0,
        "en": {
            "description" : "Overspeed",
            "cause" : "1. Error de cableado de secuencia de fase U V W 2. Umbral de juicio de falla de sobrevelocidad establecido demasiado pequeño 3. Sobreimpulso de velocidad del motor 4. Daños en la unidad",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 65296,
        "level": 0,
        "en": {
            "description" : "Pulse output overspeed",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 65282,
        "level": 0,
        "en": {
            "description" : "Failure to identify angles",
            "cause" : "El codificador del motor no pudo ponerlo a cero",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 9040,
        "level": 0,
        "en": {
            "description" : "Drive overload",
            "cause" : "Hay un desajuste entre el motor y la potencia de accionamiento",
            "solution" : "Replace the driver"
        }
    },
    {
        "id":29056,
        "level": 0,
        "en": {
            "description" : "Motor overload",
            "cause" : "1. La carga es demasiado pesada, el par efectivo excede el par nominal y continúa funcionando durante mucho tiempo. 2. Un mal ajuste de ganancia conduce a la acción de vibración y oscilación. El motor vibra y emite sonidos anormales. 3. El cableado del motor está incorrecto y roto. 4. La máquina está sujeta a colisión, la máquina de repente se vuelve más pesada y la máquina se retuerce.",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 28961,
        "level": 0,
        "en": {
            "description" : "Overheating protection for blocked motors",
            "cause" : "1. El motor está atascado mecánicamente 2. La salida del controlador U V W está desfasada o la secuencia de fase es incorrecta",
            "solution" : "Check whether the hardware is working properly, or contact technical support engineer"
        }
    },
    {
        "id": 17168,
        "level": 0,
        "en": {
            "description" : "Radiator overheating",
            "cause" : "1. La temperatura ambiente es demasiado alta, 2. El ventilador de accionamiento está dañado, 3. El servoaccionamiento está defectuoso internamente",
            "solution" : "Drop the environment temperature, or contact technical support engineer"
        }
    },
        {
        "id": 29571,
        "level": 0,
        "en": {
            "description" : "Encoder battery failure",
            "cause" : "1. Durante el corte de energía, el codificador no está conectado a la batería 2. El voltaje de la batería del codificador es demasiado bajo",
            "solution" : "Connect battery, or contact technical support engineer"
        }
    },
    {
        "id": 29490,
        "level": 0,
        "en": {
            "description" : "Encoder multi-turn count error",
            "cause" : "Fallo del codificador",
            "solution" : "Replace the motor"
        }
    },
        {
        "id": 29491,
        "level": 0,
        "en": {
            "description" : "Encoder multi-turn count overflow",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 29492,
        "level": 0,
        "en": {
            "description" : "Encoder interference",
            "cause" : "La señal Z del codificador se multiplica, lo que hace que el ángulo correspondiente de la señal Z cambie demasiado",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 29493,
        "level": 0,
        "en": {
            "description" : "External encoder scale failure",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 29494,
        "level": 0,
        "en": {
            "description" : "Encoder data abnormalities",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 29495,
        "level": 0,
        "en": {
            "description" : "Encoder return checksum exception",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 29496,
        "level": 0,
        "en": {
            "description" : "Loss of encoder Z signal",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 34321,
        "level": 0,
        "en": {
            "description" : "Excessive position deviation",
            "cause" : "1. El motor no gira 2. La ganancia del controlador es demasiado pequeña 3. La configuración H0A.08 es demasiado pequeña en relación con las condiciones de funcionamiento",
            "solution" : "Check whether the motor is working properly, or contact technical support engineer"
        }
    },
    {
        "id": 34322,
        "level": 0,
        "en": {
            "description" : "Position command too large",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 34323,
        "level": 0,
        "en": {
            "description" : "Excessive deviation from fully closed-loop position",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 25380,
        "level": 0,
        "en": {
            "description" : "Electronic gear setting overrun",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 25381,
        "level": 0,
        "en": {
            "description" : "Wrong parameter setting for fully closed loop function",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 25382,
        "level": 0,
        "en": {
            "description" : "Software position upper and lower limits set incorrectly",
            "cause" : "El valor establecido en el diccionario de objetos 0x607D-01h es menor que el valor de 0x607D-02h",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 25383,
        "level": 0,
        "en": {
            "description" : "Wrong home position offset setting",
            "cause" : "El valor de desplazamiento de origen está fuera de los límites superior e inferior de la posición del software",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 30083,
        "level": 0,
        "en": {
            "description" : "Loss of synchronisation",
            "cause" : "Durante la comunicación síncrona, se pierde la señal de sincronización de maestra",
            "solution" : ""
        }
    },
        {
        "id": 30081,
        "level": 0,
        "en": {
            "description" : "Unburned XML configuration file",
            "cause" : "El archivo de configuración del dispositivo no se ha grabado",
            "solution" : "Burn the XML configuration file"
        }
    },
    {
        "id": 65298,
        "level": 0,
        "en": {
            "description" : "Network initialization failure",
            "cause" : "1. El firmware de la FPGA no está flasheado 2. El archivo de configuración del dispositivo no está grabado 3. La unidad está defectuosa",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 30082,
        "level": 0,
        "en": {
            "description" : "Sync cycle configuration error",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 30084,
        "level": 0,
        "en": {
            "description" : "Excessive synchronisation period error",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 25384,
        "level": 0,
        "en": {
            "description" : "Fault in crossover pulse output setting",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 65521,
        "level": 0,
        "en": {
            "description" : "Zero return timeout fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 29570,
        "level": 0,
        "en": {
            "description" : "Encoder battery warning",
            "cause" : "El voltaje de la batería es inferior a 3,0 V",
            "solution" : "Replace battery"
        }
    },
    {
        "id": 21570,
        "level": 0,
        "en": {
            "description" : "DI emergency brake",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 12851,
        "level": 0,
        "en": {
            "description" : "Motor overload warning",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 12817,
        "level": 0,
        "en": {
            "description" : "Brake resistor overload alarm",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 25385,
        "level": 0,
        "en": {
            "description" : "External braking resistor too small",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 13105,
        "level": 0,
        "en": {
            "description" : "Motor power cable disconnection",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
        {
        "id": 25386,
        "level": 0,
        "en": {
            "description" : "Change of parameters requires re-powering to take effect",
            "cause" : "Los parámetros modificados pertenecen a los parámetros que surten efecto cuando la alimentación está apagada",
            "solution" : "Clear the alarm and power on again"
        }
    },
    {
        "id": 30208,
        "level": 0,
        "en": {
            "description" : "Frequent parameter storage",
            "cause" : "El sistema informático host vuelve a cambiar repetidamente los parámetros",
            "solution" : "Check whether the upper computer is working normal, or contact technical support engineer"
        }
    },

            {
        "id": 21571,
        "level": 0,
        "en": {
            "description" : "Forward overtravel warning",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 21572,
        "level": 0,
        "en": {
            "description" : "Reverse overtravel warning",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 29569,
        "level": 0,
        "en": {
            "description" : "Internal failure of the encoder",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 12597,
        "level": 0,
        "en": {
            "description" : "Input phase failure warning",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 65432,
        "level": 0,
        "en": {
            "description" : "Zero return mode setting error",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 65344,
        "level": 0,
        "en": {
            "description" : "Parameter recognition failure",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },

    {
        "id": 21121,
        "level": 0,
        "en": {
            "description" : "internal error",
            "cause" : "Restablecimiento del perro guardián",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 29956,
        "level": 0,
        "en": {
            "description" : "FPGA configuration error",
            "cause" : "Error en la inicialización de FPGA",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 51020,
        "level": 0,
        "en": {
            "description" : "Driver board identification error",
            "cause" : "PowerID es incorrecto",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 29568,
        "level": 0,
        "en": {
            "description" : "Encoder connection error",
            "cause" : "1. El enchufe del codificador está suelto 2. El tipo de codificador está configurado incorrectamente 3. El codificador del motor está dañado 4. El controlador está defectuoso",
            "solution" : "Check the cable connection of encoder, or contact technical support engineer"
        }
    },
    {
        "id": 8992,
        "level": 0,
        "en": {
            "description" : "Software overcurrent",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 9088,
        "level": 0,
        "en": {
            "description" : "Current zero point too large",
            "cause" : "Falló el arranque del módulo de muestreo actual",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 30080,
        "level": 0,
        "en": {
            "description" : "EtherCAT communication failure",
            "cause" : "La comunicación EtherCAT está desconectada",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 33921,
        "level": 0,
        "en": {
            "description" : "Excessive speed tracking error",
            "cause" : "1. Parada del motor 2. Desconexión de salida UVW 3. Límite de salida de par 4. El ajuste de ganancia del controlador es demasiado pequeño 5. Daños en el controlador o el motor",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 21120,
        "level": 0,
        "en": {
            "description" : "STO Warning",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 21569,
        "level": 0,
        "en": {
            "description" : "Upper and lower board connection failure",
            "cause" : "La placa de control del servo está conectada a la placa del controlador de manera anormal",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 8980,
        "level": 0,
        "en": {
            "description" : "Busbar overcurrent",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 17169,
        "level": 0,
        "en": {
            "description" : "Damaged or uninstalled temperature measuring resistors",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
    {
        "id": 29572,
        "level": 0,
        "en": {
            "description" : "Encoder Eeprom reading CRC fault",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    },
            {
        "id": 12928,
        "level": 0,
        "en": {
            "description" : "Servo and motor power matching faults",
            "cause" : "",
            "solution" : "System error, please contact technical support engineer"
        }
    }
]