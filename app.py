import os
from flask import Flask, render_template, request
from geometry import *
from PIL import Image

app = Flask(__name__) 




@app.route('/')
def welcome():
    #return "Hello, World!"
    return render_template('welcome.html')


@app.route('/bonjour/<string:name>')
def bonjour(name:str):
    return f"Bonjour {name}"

@app.route('/submit', methods=['POST'])
def submit():
    try:        
        nb_side = int(request.form['nb_side'])  # ou request.form.get('username')
        nb_repet = int(request.form['nb_repet'])
        init_size = int(request.form['init_size'])
        rotation_angle = int(request.form['rotation_angle'])
        color = str(request.form['color'])
    except ValueError:
        return "Erreur : nombre invalide."
    
    output = f"Nb côté demandé {nb_side}<br>"
    output += f"Nb de répétition demandé {nb_repet}<br>"
    output += f"La taille initiale du motif {init_size}<br>"
    output += f"La rotation entre chaque répétion demandé {rotation_angle}<br>"
    output += f"La couleur du motif demandé {color}<br>"

    menu_generate(nb_side, nb_repet, init_size, rotation_angle, color)
    
    if os.path.exists('static/shape.png'):
        return render_template('welcome.html', image_url='static/shape.png')
    else:
        return "Erreur : image non générée."
    

    return render_template('welcome.html', image_url='static/shape.png')


@app.route('/submit2', methods=['POST'])
def index():
    result = None
    if request.method == 'POST':
        nb_side = int(request.form['nb_side'])
        match nb_side:
            case 3:
                result = "triangle"
            case 4:
                result = "carré"
            case _:
                result = "autre forme"
    return render_template('welcome.html', result=result)

