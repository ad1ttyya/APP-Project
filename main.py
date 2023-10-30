from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Prod_listing(db.Model):
    Listing_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Prod_Name: Mapped[str] = mapped_column(String)
    Prod_Price: Mapped[str] = mapped_column(String)
    Prod_Img: Mapped[str] = mapped_column(Integer)


db = SQLAlchemy(model_class=Prod_listing)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql:root:root@localhost/shopez'

db.init_app(app)



@app.route('/')
def index():
    return render_template('index.html')
@app.route('/cart')
def cart():
    return render_template('cart.html')
@app.route('/item')
def item():
    return render_template('Item.html')
if __name__ == "__main__":
    app.run(debug=True)