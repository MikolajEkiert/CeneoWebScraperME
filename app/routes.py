from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/extract')
def extract():
    return render_template("extract.html")

@app.route('/products')
def products():
    return render_template("products.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/product')
def product():
    return render_template("product.htm , product_id = product_id")

@app.route('/name/<product_id>')
def name(name):
    return f"Hello, {name}"