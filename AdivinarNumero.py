# Importar librerias necesarias
import random
import time
import sys
from os import system
import itertools

# Importando base de datos
from database.JugadoresTable import JugadoresTable


class AdivinarNumero:
    def __init__(self, nombre):
        self.nombre = nombre

    def typewriter_effect(self, text):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()

    def progress_bar(self):
        # Barra de progreso
        for i in range(101):
            print(f"\r[{'#' * i}{' ' * (100 - i)}] {i}%", end="")
            time.sleep(0.05)

    def spinner(self):
        # Spinner de carga
        spinner = itertools.cycle(["-", "/", "|", "\\"])
        for _ in range(50):
            sys.stdout.write(next(spinner))  # Escribe el siguiente carácter
            sys.stdout.flush()  # Limpia el buffer de salida
            time.sleep(0.1)  # Espera 0.1 segundos
            sys.stdout.write("\b")  # Retrocede el cursor

    def entry(self):
        # Entrada del nombre del jugador
        text = "¿Como te llamas?"
        self.typewriter_effect(text)
        self.nombre = input().upper()

        while self.nombre.isalpha() == False:
            text = "ERROR: El nombre debe contener solo letras."
            self.typewriter_effect(text)
            text = "¿Como te llamas?"
            self.typewriter_effect(text)
            self.nombre = input().upper()

    def presentacion(self):
        # Barra de progreso y spinner
        self.progress_bar()
        system("clear")

        # Presentación del juego
        text = """<--Bienvenido al juego de adivinar el numero secreto-->"""
        self.typewriter_effect(text)

        # Entrada del nombre del jugador
        self.entry()

        # Parrafo de introducción al juego
        system("clear")
        text = f"{self.nombre}, El juego consiste en introducir un numero hasta adivinar el numero secreto."
        self.typewriter_effect(text)

        text = "Puedes seleccionar 3 niveles distintos. Cada nivel es mayor el rango de numeros a adivinar, "
        self.typewriter_effect(text)

        text = "menor la cantidad de intentos y mayor la dificultad."
        self.typewriter_effect(text)

        self.spinner()
        system("clear")
        text = "Empezando el juego..."
        self.typewriter_effect(text)
        time.sleep(2)
        system("clear")

    def nivelDelJuego(self):
        # Gestionar los niveles del juego
        text = "Selecciona un nivel de dificultad:"
        self.typewriter_effect(text)
        text = "1. Facil (1-100)"
        self.typewriter_effect(text)
        text = "2. Medio (1-500)"
        self.typewriter_effect(text)
        text = "3. Dificil (1-1000)"
        self.typewriter_effect(text)

        nivel = input("Ingrese el numero del nivel: ")
        while nivel not in ["1", "2", "3"]:
            text = "ERROR: Nivel no valido, ingrese 1, 2 o 3."
            self.typewriter_effect(text)
            nivel = input("Ingrese el numero del nivel: ")
        system("clear")
        text = f"Has seleccionado el nivel {nivel}."
        self.typewriter_effect(text)
        time.sleep(1)
        system("clear")
        return int(nivel)

    def limiteNumeros(self, nivel):
        # Definir el limite de numeros segun el nivel
        match nivel:
            case 1:
                # Nivel facil
                limite_numeros = 100
            case 2:
                # Nivel medio
                limite_numeros = 500
            case 3:
                # Nivel dificil
                limite_numeros = 1000
        return limite_numeros

    def numeroSecreto(self, nivel):
        # Generar un numero secreto aleatorio entre 1 y 100
        match nivel:
            case 1:
                # Nivel facil
                numero_secreto = random.randint(1, 100)
            case 2:
                # Nivel medio
                numero_secreto = random.randint(1, 500)
            case 3:
                # Nivel dificil
                numero_secreto = random.randint(1, 1000)
        return numero_secreto

    def cantidadIntentos(self, nivel):
        # Definir la cantidad de intentos que el usuario tiene para adivinar el numero secreto
        match nivel:
            case 1:
                # Nivel facil
                cantidad_intentos = 8
            case 2:
                # Nivel medio
                cantidad_intentos = 6
            case 3:
                # Nivel dificil
                cantidad_intentos = 4
        return cantidad_intentos

    def cabeceraDelJuego(self, **args):
        # Cabecera del juego
        print(
            f"Jugador: {self.nombre} | Nivel: {args['nivel']} | Cantidad de intentos {args['intentos'] + 1} de {args['cantidad_intentos']} {'ultimo intento' if args['intentos'] == 7 else 'intentos'}"
        )

    def juego(self):
        self.presentacion()
        # Bucle del programa
        while True:
            #
            # Variables en uso del sistema
            # cantidad_intentos: cantidad de intentos que tiene el usuario.
            # numero_secreto: numero secreto que tiene que adivinar el usuario.
            # numero_ingresados: lista de los numeros ingresados por el usuario.
            # intentos: cantidad de intentos que el usuario ha realizado.
            # nivel: nivel del juego seleccionado por el usuario.
            # limite_numeros: limite de numeros segun el nivel seleccionado.
            #
            nivel = self.nivelDelJuego()
            limite_numeros = self.limiteNumeros(nivel)
            cantidad_intentos = self.cantidadIntentos(nivel)
            numero_secreto = self.numeroSecreto(nivel)
            numero_ingresados = []
            intentos = 0
            args = {
                "limite_numeros": limite_numeros,
                "nivel": nivel,
                "numero_secreto": numero_secreto,
                "intentos": intentos,
                "cantidad_intentos": cantidad_intentos,
            }

            # Bucle de intentos del usuario
            while args["intentos"] < cantidad_intentos:
                # cabecera del juego
                self.cabeceraDelJuego(**args)

                # Solicitar al usuario que ingrese un numero
                numero = input("Ingrese un numero: ")
                while numero.isdigit() == False:
                    print("ERROR: la variable ingresada no es un numero.")
                    numero = input("Ingrese un numero: ")
                numero_ingresados.append(numero)
                numero = int(numero)

                # Validar que el numero ingresado este dentro del rango
                if numero < 1 or numero > limite_numeros:
                    print(f"ERROR: el numero debe estar entre 1 y {limite_numeros}.")
                    continue

                # Contando la cantidad de intentos
                args["intentos"] += 1

                # Verificar si el numero ingresado es igual al numero secreto
                if numero == numero_secreto:
                    system("clear")
                    text = f"¡Felicidades {self.nombre}! Has ganado el numero secreto era {numero_secreto}. Lo has hecho en {args['intentos']} de {cantidad_intentos} intento."
                    self.typewriter_effect(text)
                    text = "Presiona Enter para continuar..."
                    self.typewriter_effect(text)
                    input()

                    # Guardar el resultado en la base de datos
                    JugadoresTable().create(
                        {
                            "nombre": self.nombre,
                            "nivel": args["nivel"],
                            "intentos": args["intentos"],
                            "resultado": "ganador",
                        }
                    )
                    break

                # Verificar si el numero ingresado es mayor o menor al numero secreto
                if numero > numero_secreto:
                    print(
                        f"Lo siento {self.nombre}, El numero ingresado es mayor al numero secreto. Tienes {args['intentos']} de {cantidad_intentos} intentos"
                    )
                elif numero < numero_secreto:
                    print(
                        f"Lo siento {self.nombre}, El numero ingresado es menor al numero secreto. Tienes {args['intentos']} de {cantidad_intentos} intentos"
                    )

                # Verificar si el usuario ha agotado sus intentos
                if args["intentos"] == cantidad_intentos:
                    system("clear")
                    print(
                        f"Lo siento {self.nombre}, has perdido. El numero secreto era [{numero_secreto}]"
                    )
                    print("Numeros ingresados")
                    for intentos, numero_ingresado in enumerate(numero_ingresados):
                        print(f"Intento {intentos+1}: {numero_ingresado}")
                    text = "Presiona Enter para continuar..."
                    self.typewriter_effect(text)
                    input()

                    # Guardar el resultado en la base de datos
                    JugadoresTable().create(
                        {
                            "nombre": self.nombre,
                            "nivel": args["nivel"],
                            "intentos": args["intentos"],
                            "resultado": "perdedor",
                        }
                    )
                # Preguntar al usuario si desea seguir intentando
                if args["intentos"] < cantidad_intentos:
                    respuesta = input("¿Deseas seguir intentando? (s/n): ").lower()
                    if respuesta == "s":
                        system("clear")
                        continue
                    if respuesta == "n":
                        break

            system("clear")

            # Preguntar al usuario si desea jugar de nuevo
            text = "¿Deseas jugar de nuevo? (s/n)"
            self.typewriter_effect(text)
            respuesta = input().lower()

            # Validación de la respuesta
            while respuesta not in ["s", "n"]:
                text = "ERROR: Respuesta no valida, ingrese 's' = si o 'n' = no."
                self.typewriter_effect(text)
                text = "¿Deseas jugar de nuevo? (s/n)"
                self.typewriter_effect(text)
                respuesta = input().lower()

            # Reiniciar el juego o salir
            if respuesta == "s":
                system("clear")
                text = "Reiniciando el juego..."
                self.typewriter_effect(text)
                self.spinner()
                system("clear")
                self.entry()
                system("clear")
                continue

            # Si la respuesta es 'n', salir del juego
            elif respuesta == "n":
                system("clear")
                text = f"Gracias por jugar, {self.nombre}. ¡Hasta la próxima!"
                self.typewriter_effect(text)
                break

    def allWinner(self):
        # Mostrar todos los jugadores ganadores
        system("clear")
        text = "Jugadores ganadores:"
        self.typewriter_effect(text)
        jugadores = JugadoresTable().allWinner()
        if not jugadores:
            text = "No hay jugadores ganadores."
            self.typewriter_effect(text)
        else:
            for jugador in jugadores:
                print(
                    f"Nombre: {jugador[1]}, Nivel: {jugador[2]}, Intentos: {jugador[3]}, Resultado: {jugador[4]}"
                )
        input("Presiona Enter para continuar...")

    def allLoser(self):
        # Mostrar todos los jugadores perdedores
        system("clear")
        text = "Jugadores perdedores:"
        self.typewriter_effect(text)
        jugadores = JugadoresTable().allLoser()
        if not jugadores:
            text = "No hay jugadores perdedores."
            self.typewriter_effect(text)
        else:
            for jugador in jugadores:
                print(
                    f"Nombre: {jugador[1]}, Nivel: {jugador[2]}, Intentos: {jugador[3]}, Resultado: {jugador[4]}"
                )
        input("Presiona Enter para continuar...")

    def main(self):
        # Menu del juego
        while True:
            system("clear")
            text = "*--Consola de Juego--*"
            self.typewriter_effect(text)
            text = "Selecciona una opcion:"
            self.typewriter_effect(text)
            text = "0. Base de datos"
            self.typewriter_effect(text)
            text = "1. Jugar"
            self.typewriter_effect(text)
            text = "2. Ganadores"
            self.typewriter_effect(text)
            text = "3. Perdedores"
            self.typewriter_effect(text)
            text = "4. Salir"
            self.typewriter_effect(text)

            opcion = input("Ingrese el numero de la opcion: ")
            while opcion not in ["0", "1", "2", "3", "4"]:
                text = "ERROR: Opcion no valida, ingrese del 0 al 4."
                self.typewriter_effect(text)
                opcion = input("Ingrese el numero de la opcion: ")

            match opcion:
                case "0":
                    system("clear")
                    JugadoresTable().createDatabase()
                    text = "Presiona Enter para continuar..."
                    self.typewriter_effect(text)
                    input()
                    continue
                case "1":
                    system("clear")
                    self.juego()
                case "2":
                    system("clear")
                    self.allWinner()
                case "3":
                    system("clear")
                    self.allLoser()
                case "4":
                    system("clear")
                    text = f"Gracias por jugar. ¡Hasta la próxima!"
                    self.typewriter_effect(text)
                    return False


AdivinarNumero = AdivinarNumero("")
AdivinarNumero.main()
