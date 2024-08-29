# LogicaProgramacion
Deberes de Lógica de Programación
Nombre: Andres Alejandro Montesdeoca Cruz
Fecha 29/08/2024

# Evaluacion Contacto con el docente
Se escogio el juego de piedra papel o tijera
El proposito del juego de piedra papel o tijera: Es un juego donde compites con otra persona, en este caso la maquina y tienes 3 opciones para escoger que son Piedra, Papel, Tijera. Ambos jugadores escogen una de las 3 opciones y la opcion que sea mejor frente al adversario es el que gana.
Para esto es necesario saber que opcion es mejor de acuerdo al siguiente detalle: Piedra le gana a tijera, Tijera le gana a papel, Papel le gana a piedra y en caso de que ambos jugadores tengan la misma eleccion abra un empate.

#Objetivo del Programa
Brindar una experiencia unica al momento de jugar, asi como entretener al usuario por medio del juego de Piedra, Papel o tijera.
El programa fue diseñado en base a las reglas anteriormente mencionadas añadiendo que el jugador tiene 3 vidas en caso de perderlas todas, pierde definitivamente y vasta con una vez que gane para ser el ganador de este juego, cabe indicar que al haber empate al jugador no se le restan vidas.

#Explicacion de las principales funcionalidades

import random
# Mensaje de Bienvenida del juego
print ("Bienvenido al juego de Piedra, Papel o Tijera")
En estas sentencias tenemos la sentencia import random que nos sirve para importar la libreria random que la usaremos para generar un numero al azar, y mandamos a imprimir un mensaje de Bienvenida al juego

# Ingreso de nombre y eleccion del jugador
nombre = input("Introdcir su nombre: ")
print ("Hola",nombre, "Tiene 3 vidas para jugar")
Sentencias donde se pide al usuario ingrese su nomnre, y se imprime un recordatoria al usuario de que tiene 3 vidas para jugar

i=0
while i<3:
    print ("Escoja su eleccion: ")
    eleccion_jugador = int(input("Piedra=1 Papel=2 Tijera=3 "))
# Eleccion aleatoria de la maquina
    eleccion_pc= random.randint(1,3)
    print ("La maquina escogio", eleccion_pc)
Contador que iniciamos en 0, y la sentencia while que nos servira para ejecutar el programa mientras el contador sea menor a 3 o en alguna parte del ciclo con la sentencia break se finalice la misma
Pdimos al jugador que ingrese su eleccion y lo almacenamos en una variable, la eleccion de la maquina se hace al azar y se la almacena en una variable, ademas se imprime al usuario cual fue esta eleccion al azar

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

Condicionales dentro del ciclo while que van a comparar las elecciones del jugador como la del usuario y en ser el caso de ganar el usuario finalizar el juego rompiendo el ciclo con un break, de haber empate el ciclo vuelve a iniciar sin perder vidas, y si la maquina es la ganadora se repite el ciclo aumentando el contador en uno.

if i==3:
    print(nombre,"Usted pierde definitivamente no le quedan mas vidas")
Condicional fuera del ciclo que compara el contador si este es igual a 3 quiere decir que perdio todas sus vidas por lo tanto el usuario hace Game over.




    
