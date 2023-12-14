from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from databasecon import *
app = Flask(__name__)
get_listing()
@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html',items=items)
@app.route('/cart', methods = ['GET', 'POST'])
def cart():
    return render_template('cart.html')
@app.route('/item', methods = ['GET', 'POST'])
def item():
    return render_template('Item.html')
if __name__ == "__main__":
    app.run(debug=True)