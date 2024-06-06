import cmd
import threading
from Api.dobot_api import DobotApiDashboard, DobotApiMove, DobotApi
from time import sleep

class RobotController(cmd.Cmd):
    prompt = '(robot) '
    intro = "Bienvenido a la interfaz de control del robot. Escribe ? para listar los comandos disponibles."

    def __init__(self, dashboard, move, feed):
        super().__init__()
        self.dashboard = dashboard
        self.move = move
        self.feed = feed

    def do_enable(self, arg):
        "Habilita el robot: enable"
        self.dashboard.EnableRobot()
        print("Robot habilitado")

    def do_disable(self, arg):
        " el robot: disable"
        self.dashbDeshabilitaoard.DisableRobot()
        print("Robot deshabilitado")

    def do_move(self, arg):
        "Mueve el robot a una posición especificada: move x y z r"
        try:
            args = arg.split()
            if len(args) != 4:
                print("Error: Debes proporcionar cuatro parámetros x, y, z, r")
                return
            x, y, z, r = map(float, args)
            self.move.MovL(x, y, z, r)
            print(f"Moviendo el robot a la posición x={x}, y={y}, z={z}, r={r}")
        except ValueError:
            print("Error: Todos los parámetros deben ser números")

    def do_movej(self, arg):
        "Mueve el robot a una posición especificada usando joints: movej j1 j2 j3 j4"
        try:
            args = arg.split()
            if len(args) != 4:
                print("Error: Debes proporcionar cuatro parámetros j1, j2, j3, j4")
                return
            j1, j2, j3, j4 = map(float, args)
            self.move.MovJ(j1, j2, j3, j4)
            print(f"Moviendo el robot a las posiciones de joints j1={j1}, j2={j2}, j3={j3}, j4={j4}")
        except ValueError:
            print("Error: Todos los parámetros deben ser números")

    def do_set_speed(self, arg):
        "Configura la velocidad de movimiento del robot: set_speed speed"
        try:
            speed = float(arg)
            self.move.SetSpeed(speed)
            print(f"Velocidad configurada a {speed}")
        except ValueError:
            print("Error: El parámetro debe ser un número")

    def do_set_acceleration(self, arg):
        "Configura la aceleración del robot: set_acceleration acceleration"
        try:
            acceleration = float(arg)
            self.move.SetAcceleration(acceleration)
            print(f"Aceleración configurada a {acceleration}")
        except ValueError:
            print("Error: El parámetro debe ser un número")

    def do_circle(self, arg):
        "Realiza un movimiento circular: circle x1 y1 z1 r1 x2 y2 z2 r2"
        try:
            args = arg.split()
            if len(args) != 8:
                print("Error: Debes proporcionar ocho parámetros x1, y1, z1, r1, x2, y2, z2, r2")
                return
            x1, y1, z1, r1, x2, y2, z2, r2 = map(float, args)
            self.move.Circle(x1, y1, z1, r1, x2, y2, z2, r2)
            print(f"Moviendo el robot en un círculo desde ({x1}, {y1}, {z1}, {r1}) hasta ({x2}, {y2}, {z2}, {r2})")
        except ValueError:
            print("Error: Todos los parámetros deben ser números")

    def do_set_do(self, arg):
        "Configura una salida digital: set_do index status"
        try:
            args = arg.split()
            if len(args) != 2:
                print("Error: Debes proporcionar dos parámetros index y status")
                return
            index, status = map(int, args)
            self.dashboard.DO(index, status)
            print(f"Salida digital {index} configurada a {status}")
        except ValueError:
            print("Error: Ambos parámetros deben ser números enteros")

    def do_get_position(self, arg):
        "Obtiene la posición actual del robot: get_position"
        position = self.dashboard.GetFeed()
        print(f"Posición actual: {position}")

    def do_exit(self, arg):
        "Sale de la interfaz de control del robot: exit"
        print("Saliendo de la interfaz de control del robot")
        return True

def connect_robot():
    try:
        ip = "192.168.1.6"
        dashboard_p = 29999
        move_p = 30003
        feed_p = 30004
        print("Conectando...")
        dashboard = DobotApiDashboard(ip, dashboard_p)
        move = DobotApiMove(ip, move_p)
        feed = DobotApi(ip, feed_p)
        print(">.< La conexión se ha realizado correctamente >!<")
        return dashboard, move, feed
    except Exception as e:
        print(":( Conexión fallida :(")
        raise e

if __name__ == '__main__':
    dashboard, move, feed = connect_robot()
    RobotController(dashboard, move, feed).cmdloop()
