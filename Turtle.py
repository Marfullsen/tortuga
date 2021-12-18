#Importante, No abrir con IDE
#Por Enzzo Ayala
import turtle
import sys
import os
turtle.setup(800,600) #posicion inicial de la tortuga
turtle.shape("turtle") #forma de la tortuga
turtle.color("green") #color de la tortuga
turtle.left(90)
print("Bienvenido a Logo")
texto=[0]*7 #Texto de ayuda
texto[0]="COMANDOS"
texto[1]="av x para mover x adelante"
texto[2]="re x para retroceder x"
texto[3]="i x para girar a la izquierda x grados"
texto[4]="d x para girar a la derecha x grados"
texto[5]="casa para que la tortuga vuelva al inicio"
texto[6]="salir para salir de LOGO"
def ayuda(): #Muestra ayuda por pantalla
    for i in range(len(texto)):
        print(texto[i])
ayuda() #muestra la ayuda por primera vez
while (True): #bucle principal del juego
    pantalla=turtle.Screen()
    pantalla.bgcolor("lightblue") #color del fondo de pantalla
    pantalla.title("LOGO") #titulo de pantalla
    x=input(">>")
    if(x=="exit" or x=="salir"): #para salir
        sys.exit()
    else:
        x=x.split() #separa input por espacio
        if(x[0]=="av"): #avanza------comienzo de comandos de juego
            turtle.forward(int(x[1]))
        elif(x[0]=="d"):#gira a la derecha
            turtle.right(int(x[1]))
        elif(x[0]=="i"):#gira a la izquierda
            turtle.left(int(x[1]))
        elif(x[0]=="re"):#retrocede
            turtle.backward(int(x[1]))
        elif(x[0]=="casa" or x[0]=="home"): #retorna tortuga a casa
            turtle.home()
            turtle.left(90)
        elif(x[0]=="ayuda" or x[0]=="help"): #muestra ayuda
            ayuda()
        elif((x[0]=="limpiar" and x[1]=="consola") or (x[0]=="cls" or x[0]=="clear")): #limpia consola
            os.system("cls")
