#Control de errores de los servos
alarm_servo_list = [
    {
        "id": 0,
        "level": 0,
        "en": {
            "description" : "No hay error.",
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
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 21120,
        "level": 0,
        "en": {
            "description" : "Errores de configuración lógica programable.",
            "cause" : "1.Incompatibilidad entre las versiones del software de FPGA y MCU 2.Falla en la FPGA",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29953,
        "level": 0,
        "en": {
            "description" : "Versión del software de FPGA demasiado baja.",
            "cause" : "",
            "solution" : "Por favor, contacta con un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29954,
        "level": 0,
        "en": {
            "description" : "Fallo en la interrupción de la lógica programable",
            "cause" : "1.Falla en la FPGA 2.Anomalía en el handshake de comunicación entre FPGA y MCU 3.Tiempo de cálculo interno del controlador excedido",
            "solution" : "If connecting the power for many times, the alarm is still reported, please replace the drive"
        }
    },
    {
        "id": 25377,
        "level": 0,
        "en": {
            "description" : "Excepciones internas del programa",
            "cause" : "1.Falla en la EEPROM 2.Falla en el servodrive",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 21808,
        "level": 0,
        "en": {
            "description" : "Fallo en el almacenamiento de parámetros",
            "cause" : "1.Anomalía durante la escritura de parámetros 2.Anomalía durante la lectura de parámetros",
            "solution" : "Restablezca los parámetros y vuelva a encender, o por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 28962,
        "level": 0,
        "en": {
            "description" : "Fallos de coincidencia de producto",
            "cause" : "1.El número de serie del producto (motor o controlador) no existe 2.Incompatibilidad en el nivel de potencia entre el motor y el controlador",
            "solution" : "1.Verifique si los parámetros del motor coinciden con el modelo del motor en la placa de características. 2.Verifique si el motor y el controlador coinciden; de lo contrario, seleccione el motor y el controlador adecuados."
        }
    },
    {
        "id": 21574,
        "level": 0,
        "en": {
            "description" : "Fallo de comando de activación de servo no válido",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 28964,
        "level": 0,
        "en": {
            "description" : "Fallo de coincidencia de producto en modo de posición absoluta",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 25378,
        "level": 0,
        "en": {
            "description" : "Asignación repetida de funciones de DI",
            "cause" : "1.Al asignar funciones DI, la misma función se asigna repetidamente a varios terminales DI 2.El número de función DI excede la cantidad de funciones DI disponibles 3.La función DI no es compatible",
            "solution" : "1. Verifique si la misma función está asignada a diferentes DI. 2.Confirme si el MCU correspondiente soporta la funcionalidad asignada."
        }
    },
    {
        "id": 25379,
        "level": 0,
        "en": {
            "description" : "Desbordamiento en la asignación de funciones DO",
            "cause" : "1.Anomalía en el controlador 2.Contacto deficiente o desconexión del cable de comunicación 3.El cable de comunicación no está conectado a tierra o la conexión a tierra es deficiente",
            "solution" : "Verifique si el motor y el circuito están funcionando correctamente, o contacte con un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29488,
        "level": 0,
        "en": {
            "description" : "Los datos en la ROM del encoder del motor están siendo incorrectamente verificados o los parámetros no se han almacenado correctamente.",
            "cause" : "",
            "solution" : "Error del sistema, póngase en contacto con el ingeniero de soporte técnico"
        }
    },
    {
        "id": 8752,
        "level": 0,
        "en": {
            "description" : "Corriente excesiva en hardware",
            "cause" : "1. El comando de entrada está sincronizado con el servo de encendido y encendido o el comando de entrada es demasiado rápido 2. La resistencia de frenado es demasiado pequeña o está en cortocircuito 3. El cable del motor no está en buen contacto 4. El cable del motor está conectado a tierra 5. El cable UVW del motor está en cortocircuito 6. El motor está quemado 7. El ajuste de ganancia no es razonable y el motor oscila 8. El codificador está cableado incorrectamente, envejecido y corrosión, y el enchufe del codificador está suelto 9. El controlador está defectuoso",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 8977,
        "level": 0,
        "en": {
            "description" : "Fallo por sobrecarga de corriente en el eje DQ",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 65288,
        "level": 0,
        "en": {
            "description" : "Tiempo de espera de la operación de muestreo del sistema FPGA",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 9024,
        "level": 0,
        "en": {
            "description" : "Salida cortocircuitada a tierra",
            "cause" : "1.Cortocircuito a tierra en los cables de potencia del controlador (U V W) 2.Cortocircuito a tierra en el motor 3.Falla en el controlador",
            "solution" : "Por favor, contacta con un ingeniero de soporte técnico."
        }
    },
    {
        "id": 13184,
        "level": 0,
        "en": {
            "description" : "Error de secuencia de fases UVW",
            "cause" : "La secuencia de fases U V W del motor no corresponde con la de U V W del controlador",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        },
    },
        {
        "id": 33922,
        "level": 0,
        "en": {
            "description" : "Flying Cars",
            "cause" : "1. Error de cableado de secuencia de fase U V W 2. Al encender, la señal de interferencia causa el error de detección de fase inicial del rotor del motor 3. El modelo del codificador es incorrecto o un error de cableado 4. El cableado del codificador está suelto 5. La carga es demasiado grande",
            "solution" : "Por favor, contacta con un ingeniero de soporte técnico."
        }
    },
    {
        "id": 12816,
        "level": 0,
        "en": {
            "description" : "Sobrevoltaje eléctrico en el circuito principal",
            "cause" : "1.Nivel de voltaje de entrada incorrecto 2.Falla en la resistencia de frenado 3.Resistencia de frenado demasiado grande, la velocidad de absorción de energía es demasiado lenta",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 12832,
        "level": 0,
        "en": {
            "description" : "Subvoltaje en el circuito principal",
            "cause" : "1.Voltaje de entrada de la fuente de alimentación inestable o pérdida de energía 2.Caída de voltaje significativa durante una aceleración brusca 3.Falla en el servodrive",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
     {
        "id": 12592,
        "level": 0,
        "en": {
            "description" : "Escasez eléctrica en el circuito principal",
            "cause" : "1. Potencia de entrada R S T Faltan 2 fases 2. La unidad está dañada",
            "solution" : "Verifique la conexión del cable de alimentación; de lo contrario, reemplace el controlador."
        }
    },
        {
        "id": 12576,
        "level": 0,
        "en": {
            "description" : "Control de subvoltaje eléctrico",
            "cause" : "1. La fuente de alimentación de control es inestable o está apagada; 2. El cable de control está en mal contacto",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 33920,
        "level": 0,
        "en": {
            "description" : "Exceso de velocidad",
            "cause" : "1. Error de cableado de secuencia de fase U V W 2. Umbral de juicio de falla de sobrevelocidad establecido demasiado pequeño 3. Sobreimpulso de velocidad del motor 4. Daños en la unidad",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 65296,
        "level": 0,
        "en": {
            "description" : "Sobrevelocidad de salida de pulsos",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 65282,
        "level": 0,
        "en": {
            "description" : "Fallo en la identificación de ángulos",
            "cause" : "El codificador del motor no pudo ponerlo a cero",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 9040,
        "level": 0,
        "en": {
            "description" : "Sobrecarga del controlador",
            "cause" : "Hay un desajuste entre el motor y la potencia de accionamiento",
            "solution" : "Reemplace el controlador"
        }
    },
    {
        "id":29056,
        "level": 0,
        "en": {
            "description" : "Sobrecarga del motor",
            "cause" : "1. La carga es demasiado pesada, el par efectivo excede el par nominal y continúa funcionando durante mucho tiempo. 2. Un mal ajuste de ganancia conduce a la acción de vibración y oscilación. El motor vibra y emite sonidos anormales. 3. El cableado del motor está incorrecto y roto. 4. La máquina está sujeta a colisión, la máquina de repente se vuelve más pesada y la máquina se retuerce.",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 28961,
        "level": 0,
        "en": {
            "description" : "Protección por sobrecalentamiento para motores bloqueados",
            "cause" : "1. El motor está atascado mecánicamente 2. La salida del controlador U V W está desfasada o la secuencia de fase es incorrecta",
            "solution" : "Verifique si el hardware está funcionando correctamente o contacte con un ingeniero de soporte técnico."
        }
    },
    {
        "id": 17168,
        "level": 0,
        "en": {
            "description" : "Sobrecalentamiento del radiador",
            "cause" : "1. La temperatura ambiente es demasiado alta, 2. El ventilador de accionamiento está dañado, 3. El servoaccionamiento está defectuoso internamente",
            "solution" : "Reduzca la temperatura del ambiente o contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 29571,
        "level": 0,
        "en": {
            "description" : "Fallo de la batería del codificador",
            "cause" : "1. Durante el corte de energía, el codificador no está conectado a la batería 2. El voltaje de la batería del codificador es demasiado bajo",
            "solution" : "Conecte la batería o contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29490,
        "level": 0,
        "en": {
            "description" : "Error en el conteo multi-vuelta del encoder",
            "cause" : "Fallo del codificador",
            "solution" : "Reemplace el motor."
        }
    },
        {
        "id": 29491,
        "level": 0,
        "en": {
            "description" : "Desbordamiento de cuenta de vueltas múltiples del encoder",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29492,
        "level": 0,
        "en": {
            "description" : "Interferencia del codificador",
            "cause" : "La señal Z del codificador se multiplica, lo que hace que el ángulo correspondiente de la señal Z cambie demasiado",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 29493,
        "level": 0,
        "en": {
            "description" : "Fallo de escala del codificador externo",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29494,
        "level": 0,
        "en": {
            "description" : "Anomalías en los datos del codificador",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 29495,
        "level": 0,
        "en": {
            "description" : "Excepción de checksum en el retorno del codificador",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29496,
        "level": 0,
        "en": {
            "description" : "Pérdida de la señal Z del codificador",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 34321,
        "level": 0,
        "en": {
            "description" : "Desviación excesiva de posición",
            "cause" : "1. El motor no gira 2. La ganancia del controlador es demasiado pequeña 3. La configuración H0A.08 es demasiado pequeña en relación con las condiciones de funcionamiento",
            "solution" : "Verifique si el motor está funcionando correctamente o contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 34322,
        "level": 0,
        "en": {
            "description" : "Comando de posición demasiado grande",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 34323,
        "level": 0,
        "en": {
            "description" : "Desviación excesiva de la posición totalmente cerrada",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 25380,
        "level": 0,
        "en": {
            "description" : "Sobrepaso en la configuración del engranaje electrónico",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 25381,
        "level": 0,
        "en": {
            "description" : "Configuración incorrecta de parámetros para la función de lazo cerrado completo",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 25382,
        "level": 0,
        "en": {
            "description" : "Los límites superiores e inferiores de posición del software están configurados incorrectamente.",
            "cause" : "El valor establecido en el diccionario de objetos 0x607D-01h es menor que el valor de 0x607D-02h",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 25383,
        "level": 0,
        "en": {
            "description" : "Configuración incorrecta del desplazamiento de la posición de inicio",
            "cause" : "El valor de desplazamiento de origen está fuera de los límites superior e inferior de la posición del software",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 30083,
        "level": 0,
        "en": {
            "description" : "Pérdida de sincronización",
            "cause" : "Durante la comunicación síncrona, se pierde la señal de sincronización de maestra",
            "solution" : ""
        }
    },
        {
        "id": 30081,
        "level": 0,
        "en": {
            "description" : "Archivo de configuración XML no grabado",
            "cause" : "El archivo de configuración del dispositivo no se ha grabado",
            "solution" : "Grabar el archivo de configuración XML"
        }
    },
    {
        "id": 65298,
        "level": 0,
        "en": {
            "description" : "Fallo en la inicialización de la red",
            "cause" : "1. El firmware de la FPGA no está flasheado 2. El archivo de configuración del dispositivo no está grabado 3. La unidad está defectuosa",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 30082,
        "level": 0,
        "en": {
            "description" : "Error en la configuración del ciclo de sincronización",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 30084,
        "level": 0,
        "en": {
            "description" : "Error de período de sincronización excesivo",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 25384,
        "level": 0,
        "en": {
            "description" : "Fallo en la configuración de salida de pulso de cruce",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 65521,
        "level": 0,
        "en": {
            "description" : "Fallo de tiempo de retorno a cero",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 29570,
        "level": 0,
        "en": {
            "description" : "Advertencia de batería del codificador",
            "cause" : "El voltaje de la batería es inferior a 3.0 V",
            "solution" : "Reemplace la batería"
        }
    },
    {
        "id": 21570,
        "level": 0,
        "en": {
            "description" : "Freno de emergencia DI",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 12851,
        "level": 0,
        "en": {
            "description" : "Advertencia de sobrecarga del motor",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 12817,
        "level": 0,
        "en": {
            "description" : "Alarma de sobrecarga del resistor de freno",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 25385,
        "level": 0,
        "en": {
            "description" : "Resistencia de frenado externa demasiado pequeña",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 13105,
        "level": 0,
        "en": {
            "description" : "Desconexión del cable de alimentación del motor",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
        {
        "id": 25386,
        "level": 0,
        "en": {
            "description" : "Los cambios de parámetros requieren que se vuelva a encender para que surtan efecto.",
            "cause" : "Los parámetros modificados pertenecen a los parámetros que surten efecto cuando la alimentación está apagada",
            "solution" : "Desactive la alarma y vuelva a encender."
        }
    },
    {
        "id": 30208,
        "level": 0,
        "en": {
            "description" : "Almacenamiento frecuente de parámetros",
            "cause" : "El sistema informático host vuelve a cambiar repetidamente los parámetros",
            "solution" : "Verifique si la computadora principal está funcionando normalmente, o contacte a un ingeniero de soporte técnico."
        }
    },

            {
        "id": 21571,
        "level": 0,
        "en": {
            "description" : "Advertencia de recorrido excesivo hacia adelante",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 21572,
        "level": 0,
        "en": {
            "description" : "Advertencia de recorrido excesivo hacia atrás",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 29569,
        "level": 0,
        "en": {
            "description" : "Fallo interno del encoder",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 12597,
        "level": 0,
        "en": {
            "description" : "Advertencia de fallo en fase de entrada",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 65432,
        "level": 0,
        "en": {
            "description" : "Error en la configuración del modo de retorno a cero",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 65344,
        "level": 0,
        "en": {
            "description" : "Fallo en el reconocimiento de parámetros",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },

    {
        "id": 21121,
        "level": 0,
        "en": {
            "description" : "Error interno",
            "cause" : "Restablecimiento del perro guardián",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 29956,
        "level": 0,
        "en": {
            "description" : "Error de configuración de FPGA",
            "cause" : "Error en la inicialización de FPGA",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 51020,
        "level": 0,
        "en": {
            "description" : "Error de identificación de placa del controlador",
            "cause" : "PowerID es incorrecto",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 29568,
        "level": 0,
        "en": {
            "description" : "Error de conexión del encoder",
            "cause" : "1. El enchufe del codificador está suelto 2. El tipo de codificador está configurado incorrectamente 3. El codificador del motor está dañado 4. El controlador está defectuoso",
            "solution" : "Verifique la conexión del cable del encoder o contacte con un ingeniero de soporte técnico."
        }
    },
    {
        "id": 8992,
        "level": 0,
        "en": {
            "description" : "Sobrecorriente de software",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 9088,
        "level": 0,
        "en": {
            "description" : "Punto cero de corriente demasiado grande",
            "cause" : "Falló el arranque del módulo de muestreo actual",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 30080,
        "level": 0,
        "en": {
            "description" : "Fallo de comunicación EtherCAT",
            "cause" : "La comunicación EtherCAT está desconectada",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 33921,
        "level": 0,
        "en": {
            "description" : "Error de seguimiento de velocidad excesiva",
            "cause" : "1. Parada del motor 2. Desconexión de salida UVW 3. Límite de salida de par 4. El ajuste de ganancia del controlador es demasiado pequeño 5. Daños en el controlador o el motor",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 21120,
        "level": 0,
        "en": {
            "description" : "Advertencia de parada segura (STO)",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 21569,
        "level": 0,
        "en": {
            "description" : "Fallo en la conexión de la placa superior e inferior",
            "cause" : "La placa de control del servo está conectada a la placa del controlador de manera anormal",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 8980,
        "level": 0,
        "en": {
            "description" : "Sobrecorriente en el busbar",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 17169,
        "level": 0,
        "en": {
            "description" : "Resistencias de medición de temperatura dañadas o no instaladas",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
    {
        "id": 29572,
        "level": 0,
        "en": {
            "description" : "Fallo de CRC en la lectura de la EEPROM del encoder",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    },
            {
        "id": 12928,
        "level": 0,
        "en": {
            "description" : "Fallas de coincidencia de potencia entre el servo y el motor",
            "cause" : "",
            "solution" : "Error del sistema, por favor contacte a un ingeniero de soporte técnico."
        }
    }
]