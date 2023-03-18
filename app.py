from flask import Flask, render_template, request, redirect, url_for
import  requests 
import random
import database_functions as db
app = Flask(__name__)

@app.route('/') 
def index():
    pokemon = add_pokemon()
    print(pokemon)
    # pokemon = [rid],["official-artwork"],["other"],["front_default"], 
    return render_template ('index.html', pokemon = pokemon)

def add_pokemon():
    pokemons = []
    for x in range(10):
        rid = random.randint(1,1001)
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{rid}')
        pokemon = response.json()
        pokemons.append(pokemon)

    return pokemons


# def index():
#     posts = db.get_all_posts ()

#     return render_template('index.html', posts = posts)

@app.route('/success', methods=['POST'])
def submit():
    name = request.form['name']
    type = (request.form['type']) 
    location = request.form['location']
    db.add_post(name, type)
  
    return render_template('success.html')

@app.route('/delete-post/<rowid>')
def delete(rowid):
    db.delete_post(rowid)
    return redirect(url_for('index'))


@app.route('/edit-post/<rowid>', methods=['POST'])
def editpost(rowid):
    name = request.form['name']
    time = (request.form['type']) 
    post = request.form['location']
    db.update_post(name, time, post, rowid)

    return redirect(url_for('index'))


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')



# @app.route('/')



# if __name__== '__main__':
#     app.run(debug=True, host='0.0.0.0')