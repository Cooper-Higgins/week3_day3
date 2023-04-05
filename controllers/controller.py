from app import app
from flask import render_template
from models.order_list import orders

@app.route('/')
def index():
    return render_template("index.html", title="CodeClan Records Admin", orders=orders)

@app.route('/orders/<int:id>')
def customer_order(id):
    return render_template("order.html", title="Customer Order Full Details", order=orders[id -1])