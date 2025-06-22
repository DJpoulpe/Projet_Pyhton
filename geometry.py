#from inspect import _void
#import turtle
#from PIL import Image



from PIL import Image
import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas



def menu_generate(nb_side: int, nb_repet: int, init_size: int, rotation_angle: int, color: str):
        return triangle(nb_side, nb_repet, init_size, rotation_angle, color)
        
        
"""
def triangle(nb_side:int, nb_repet:int, init_size: int, rotation_angle: int, color: str):
    print("i'm at the beginning of the function triangle\n")
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0, 0)  # Désactive les animations
    t = turtle.Turtle()
    t.hideturtle()       # Cache le curseur pour gagner du temps
    t.speed(0)           # Vitesse max
    #t.color(color)
    rotation_shape = calculate_rotation(nb_side)

    for _ in range(nb_repet):
        for _ in range(nb_side):
            t.forward(init_size)
            t.right(rotation_shape)
        t.right(rotation_angle)

    canvas = screen.getcanvas()
    canvas.postscript(file="static/shape.eps")  # ou .ps
    screen.bye()

    Image.open("static/shape.eps").save("static/shape.png")
    print("I'm at the end of the function triangle")


def calculate_rotation(nb_side:int):
    return int(360/nb_side)
"""

def triangle(nb_side:int, nb_repet: int, init_size: int, rotation_angle: int, color: str):
    print("Début fonction triangle")

    # Créer une fenêtre Tkinter sans affichage visible
    root = tk.Tk()
    root.withdraw()  # Cache la fenêtre principale

    # Créer un canvas pour turtle
    canvas = ScrolledCanvas(root)
    canvas.config(width=600, height=600)
    canvas.pack()

    t = RawTurtle(canvas)
    t.hideturtle()
    t.speed(0)
    #t.color(color)

    for _ in range(nb_repet):
        for _ in range(nb_side):
            t.forward(init_size)
            t.left(int(360/nb_side))
        t.left(rotation_angle)

    # Sauvegarder l’image depuis le canvas
    canvas.update()
    canvas.postscript(file="static/shape.eps")

    # Nettoyage
    t.clear()
    root.destroy()

    # Conversion en PNG
    Image.open("static/shape.eps").save("static/shape.png")

    print("Fin fonction triangle")


