from flask import Flask, render_template, request, redirect, session, jsonify
import requests
from stravalib.client import Client
import openfoodfacts
import sqlite3
import os

def init_db():
    conn = sqlite3.connect('aliments.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS aliments
                 (nom TEXT, marque TEXT, calories INTEGER)''')
    conn.commit()
    conn.close()

init_db()

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'  # À changer en production

@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mon Suivi Santé</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Mon Suivi Santé</h1>
        <div class="nav-links">
            <a href="/aliments">Rechercher un aliment</a>
            <a href="/mes-aliments">Mes aliments fréquents</a>
            <a href="/strava_auth">Connecter Strava</a>
        </div>
    </body>
    </html>
    """

@app.route('/mes-aliments', methods=['GET', 'POST'])
def mes_aliments():
    if request.method == 'POST':
        nom = request.form.get('nom')
        marque = request.form.get('marque')
        calories = request.form.get('calories')

        conn = sqlite3.connect('aliments.db')
        c = conn.cursor()
        c.execute("INSERT INTO aliments VALUES (?, ?, ?)", (nom, marque, calories))
        conn.commit()
        conn.close()

    conn = sqlite3.connect('aliments.db')
    c = conn.cursor()
    c.execute("SELECT * FROM aliments")
    aliments = c.fetchall()
    conn.close()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mes Aliments</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Mes Aliments Fréquents</h1>
        <form method="POST">
            <input type="text" name="nom" placeholder="Nom de l'aliment" required>
            <input type="text" name="marque" placeholder="Marque">
            <input type="number" name="calories" placeholder="Calories/100g" required>
            <button type="submit">Ajouter</button>
        </form>
        <div class="results">
            {generate_aliments_html(aliments)}
        </div>
    </body>
    </html>
    """

def generate_aliments_html(aliments):
    html = "<div class='mes-aliments'>"
    for aliment in aliments:
        html += f"""
            <div class='product'>
                <h3>{aliment[0]}</h3>
                <p>Marque: {aliment[1]}</p>
                <p>Calories: {aliment[2]} kcal/100g</p>
            </div>
        """
    return html + "</div>"

@app.route('/aliments', methods=['GET', 'POST'])
def recherche_aliments():
    results = ""
    if request.method == 'POST':
        query = request.form.get('query')
        api = openfoodfacts.API(user_agent="MonSuiviSante - Flask - Version 1.0")
        search_result = api.search(query)
        if search_result and 'products' in search_result:
            products_list = ""
            for product in search_result['products'][:5]:
                name = product.get('product_name', 'Sans nom')
                brand = product.get('brands', 'Marque inconnue')
                calories = product.get('nutriments', {}).get('energy-kcal_100g', 'N/A')
                products_list += f"""
                    <div class='product'>
                        <h3>{name}</h3>
                        <p>Marque: {brand}</p>
                        <p>Calories: {calories} kcal/100g</p>
                    </div>
                """
            results = f"<div class='results'><h2>Résultats pour '{query}':</h2>{products_list}</div>"
        else:
            results = "<div class='results'>Aucun résultat trouvé</div>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recherche d'aliments</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Recherche d'aliments</h1>
        <form method="POST">
            <input type="text" name="query" placeholder="Rechercher un aliment">
            <button type="submit">Rechercher</button>
        </form>
        {results}
    </body>
    </html>
    """

@app.route('/strava_auth')
def strava_auth():
    client = Client()
    authorize_url = client.authorization_url(
        client_id=os.environ.get('STRAVA_CLIENT_ID'),
        redirect_uri='https://laformepaslesformes.repl.co/strava_callback',
        scope=['read_all', 'profile:read_all', 'activity:read_all']
    )
    return redirect(authorize_url)

@app.route('/strava_callback')
def strava_callback():
    code = request.args.get('code')
    client = Client()
    token_response = client.exchange_code_for_token(
        client_id=os.environ.get('STRAVA_CLIENT_ID'),
        client_secret=os.environ.get('STRAVA_CLIENT_SECRET'),
        code=code
    )

    client.access_token = token_response['access_token']
    athlete = client.get_athlete()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Strava Connecté</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>Connecté à Strava</h1>
        <p>Bienvenue {athlete.firstname} {athlete.lastname}!</p>
        <p>Email: {athlete.email}</p>
        <a href="/">Retour à l'accueil</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)