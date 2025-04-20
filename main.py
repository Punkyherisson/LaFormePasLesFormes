
from flask import Flask, render_template, request, redirect, session
import requests
from stravalib.client import Client
import openfoodfacts

app = Flask(__name__)
app.secret_key = 'votre_clé_secrète'  # À changer en production

@app.route('/')
def index():
    return """
    <h1>Mon Suivi Santé</h1>
    <a href="/aliments">Rechercher un aliment</a><br>
    <a href="/strava_auth">Connecter Strava</a>
    """

@app.route('/aliments', methods=['GET', 'POST'])
def recherche_aliments():
    if request.method == 'POST':
        query = request.form.get('query')
        products = openfoodfacts.products.search(query)
        return f"Résultats pour {query}: {products}"
    return """
    <form method="POST">
        <input type="text" name="query" placeholder="Rechercher un aliment">
        <button type="submit">Rechercher</button>
    </form>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
