import random
# Mensaje de Bienvenida del juego
print ("Bienvenido al juego de Piedra, Papel o Tijera")
# Ingreso de nombre y eleccion del jugador
nombre = input("Introdcir su nombre: ")
print ("Hola",nombre, "Tiene 3 vidas para jugar")
print ("Escoja su eleccion: ")
eleccion_jugador = int(input("Piedra=1 Papel=2 Tijera=3 "))
# Eleccion aleatoria de la maquina
eleccion_pc= random.randint(1,3)
print ("La maquina escogio", eleccion_pc)
if eleccion_jugador == eleccion_pc:
    print ("Usted empato el juego")
    print (nombre, "No se le restaran vidas")
else:
    print("Gana o pierde")