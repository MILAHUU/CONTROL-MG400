import mysql.connector

class Database:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="",
                database="mov_dobot"
            )
            self.cursor = self.connection.cursor()
            print("Conexión establecida correctamente a la base de datos.")
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")

    def insert_directa(self, joint_1, joint_2, joint_3, joint_4, timestamp):
        try:
            sql = "INSERT INTO c_directa (joint_1, joint_2, joint_3, joint_4, timestamp) VALUES (%s, %s, %s, %s, %s)"
            values = (joint_1, joint_2, joint_3, joint_4, timestamp)
            self.cursor.execute(sql, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error al insertar en la tabla directa: {err}")

    def insert_inversa(self, coord_x, coord_y, coord_z, roll, timestamp):
        try:
            sql = "INSERT INTO c_inversa (coord_x, coord_y, coord_z, roll, timestamp) VALUES (%s, %s, %s, %s, %s)"
            values = (coord_x, coord_y, coord_z, roll, timestamp)
            self.cursor.execute(sql, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error al insertar en la tabla inversa: {err}")



    def close(self):
        self.cursor.close()
        self.connection.close()