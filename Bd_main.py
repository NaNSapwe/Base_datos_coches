import mysql.connector

#ejercicio base de datos de coches basasdo en marca modelo año (intento de uso de sql)

class Coche:

    def __innit__(self. coche_id):

        self.coche_id = coche_id
        self.marca = None
        self.modelo = None
        self.año = None
        self.cargar_desde_bd()

    def cargar_desde_bd(self):
        
        # modificar los datos para el servidor sql
        conexion = mysql.connector.connect(
            host = "",
            user = "",
            password = "",
            database = ""
        )

        coche_data =

        if coche_data:

            self.marca, self.modelo, self.año = coche_data
        
        else:

            print(f"No se encontro el coche con id {self.coche_id}")

    def detalles(self):

        if self.marca and self.modelo and self.año:

            print(f"Coche: {self.marca}, {self.modelo}, {self.año}")

        else:

            print("Detalles de coche no disponibles")