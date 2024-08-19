import random
# Mensaje de Bienvenida del juego
print ("Bienvenido al juego de Piedra, Papel o Tijera")
# Ingreso de nombre y eleccion del jugador
nombre = input("Introdcir su nombre: ")
print ("Hola",nombre, "Tiene 3 vidas para jugar")
i=0
while i<3:
    print ("Escoja su eleccion: ")
    eleccion_jugador = int(input("Piedra=1 Papel=2 Tijera=3 "))
# Eleccion aleatoria de la maquina
    eleccion_pc= random.randint(1,3)
    print ("La maquina escogio", eleccion_pc)
# Condicional donde Pc y jugador empatan el juego
    if eleccion_jugador == eleccion_pc:
        print ("Usted empato el juego")
        print (nombre, "No se le restaran vidas")
# Condicionales donde la Pc es el ganador
    elif eleccion_pc==1 and eleccion_jugador==3:
        print(nombre,"Usted Pierde, Tijera pierde contra Piedra")
        print("Se le restara una vida")
        i=i+1
    elif(eleccion_pc==2 and eleccion_jugador==1):
        print(nombre,"Usted Pierde, Piedra pierde contra Papel")
        print("Se le restara una vida")
        i=i+1
    elif(eleccion_pc==3 and eleccion_jugador==2):
        print(nombre,"Usted Pierde, Papel pierda contra Tijera")
        print("Se le restara una vida")
        i=i+1
# Condicionales donde el jugador es el ganador
    elif eleccion_jugador==1 and eleccion_pc==3:
        print(nombre,"Usted Gana, Piedra le gana a Tijera")
        break
    elif(eleccion_jugador==2 and eleccion_pc==1):
        print(nombre,"Usted Gana, Papel le gana a Piedra")
        break
    elif(eleccion_jugador==3 and eleccion_pc==2):
        print(nombre,"Usted Gana, Tijera le gana a Papel")
        break
if i==3:
    print(nombre,"Usted pierde definitivamente no le quedan mas vidas")