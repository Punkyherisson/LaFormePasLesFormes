
from flask import Flask, render_template, request, redirect, session
import requests
from stravalib.client import Client
import openfoodfacts

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
            <a href="/strava_auth">Connecter Strava</a>
        </div>
    </body>
    </html>
    """

@app.route('/aliments', methods=['GET', 'POST'])
def recherche_aliments():
    results = ""
    if request.method == 'POST':
        query = request.form.get('query')
        search_result = openfoodfacts.API().search(query)
        if search_result and 'products' in search_result:
            products_list = ""
            for product in search_result['products'][:5]:
                name = product.get('product_name', 'Sans nom')
                brand = product.get('brands', 'Marque inconnue')
                products_list += f"<div class='product'><h3>{name}</h3><p>Marque: {brand}</p></div>"
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
