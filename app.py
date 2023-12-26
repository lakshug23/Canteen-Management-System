# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

menu = [
    {'id': 1, 'name': 'Burger', 'price': 5.99},
    {'id': 2, 'name': 'Pizza', 'price': 8.49},
    {'id': 3, 'name': 'Salad', 'price': 3.99},
]

@app.route('/')
def index():
    return render_template('login.html', menu=menu)

@app.route('/menu.html')
def get_menu():
    return render_template('menu.html', menu=menu)

@app.route('/order.html')
def place_order():
    return render_template('order.html', menu=menu)

@app.route('/order_placed.html')
def order_success():
    return render_template('order_placed.html', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)
