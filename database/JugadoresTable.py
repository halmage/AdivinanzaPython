import sqlite3


class JugadoresTable:
    def createDatabase(self):
        # Crear la base de datos si no existe y crear la tabla 'operaciones' con los campos id, num1, num2, operacion y resultado
        conexion = sqlite3.connect("database/AdivinarNumero.db")
        try:
            conexion.execute(
                """
                create table jugadores (
                                    id integer primary key autoincrement,
                                    nombre text, 
                                    nivel text,
                                    intentos text,
                                    resultado text
                                )"""
            )
            print("Se creo la base de datos del juego advinanza de numeros")
        except sqlite3.OperationalError:
            print("La base de datos del juego advinanza de numeros ya existe")
        conexion.close()

    def create(self, resultado):
        # Insertar un nuevo resultado en la tabla 'operaciones'
        conexion = sqlite3.connect("database/AdivinarNumero.db")
        conexion.execute(
            "insert into jugadores(nombre,nivel,intentos,resultado) values (?,?,?,?)",
            (
                resultado["nombre"],
                resultado["nivel"],
                resultado["intentos"],
                resultado["resultado"],
            ),
        )
        conexion.commit()

    def find(self, nombre):
        # Obtener todos los jugadores almacenados en la tabla 'jugadores'
        conexion = sqlite3.connect("database/AdivinarNumero.db")
        res = conexion.execute(
            "SELECT * FROM jugadores WHERE nombre = ?", (resultado["nombre"],)
        )
        return res.fetchall()
        conexion.close()

    def allWinner(self):
        # Obtener todos los jugadores ganadores almacenados en la tabla 'jugadores'
        conexion = sqlite3.connect("database/AdivinarNumero.db")
        res = conexion.execute(
            "SELECT * FROM jugadores WHERE resultado = 'ganador' ORDER BY intentos ASC"
        )
        return res.fetchall()
        conexion.close()

    def allLoser(self):
        # Obtener todos los jugadores perdedor almacenados en la tabla 'jugadores'
        conexion = sqlite3.connect("database/AdivinarNumero.db")
        res = conexion.execute("SELECT * FROM jugadores WHERE resultado = 'perdedor'")
        return res.fetchall()
        conexion.close()
