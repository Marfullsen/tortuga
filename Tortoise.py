#Importante, No abrir con IDE
#Por FAMP
import turtle
from turtle import onkey, listen, mainloop, shape, done, onclick, goto
import sys
import os

turtle.setup(800,600) #posicion inicial de la tortuga
turtle.shape("turtle") #formas: arrow, turtle, circle, square, triangle, classic, blank
turtle.color("yellow") #color de la tortuga
turtle.bgcolor("darkgreen") #color del fondo de pantalla
turtle.title("Tortoise by FAMP") #titulo de pantalla
turtle.right(90)

move = turtle.Turtle()
move.shape("circle")
move.color("#aaffcc")

def k1():
	move.forward(45)
	turtle.back(45)
def k2():
	move.left(45)
	turtle.right(45)
def k3():
	move.right(45)
	turtle.left(45)
def k4():
	move.back(45)
	turtle.forward(45)
def k5():
        turtle.bye()
        sys.exit()
def k6():
        turtle.home()
        move.home()
def oben():
        turtle.up()
        move.up()
def unten():
        turtle.down()
        move.down()        
onkey(k1, "Up")
onkey(k2, "Left")
onkey(k3, "Right")
onkey(k4, "Down")
onkey(k5, "Escape")
onkey(k6, "h")
onkey(k6, "H")
onkey(oben, "u")
onkey(unten, "i")

move.screen.onclick(goto)
move.screen.onclick(move.goto, btn=3)
#onclick(goto, btn=3)

listen()
done()

"""while (True): #bucle principal del juego
    
    #screen.onkey(f, "Up")
    #screen.listen()
"""
"""    if(x=="Q" or x=="q"): #para salir
        sys.exit()
    else:
        #x=x.split() #separa input por espacio
        if(x=="w"): #avanza------comienzo de comandos de juego
            turtle.forward(int(20))
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
"""
