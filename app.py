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
    return render_template('index.html', menu=menu)

@app.route('/place_order', methods=['POST'])
def place_order():
    selected_items = request.form.getlist('item')
    total_price = sum(float(item['price']) for item in menu if str(item['id']) in selected_items)
    return f'Order placed successfully. Total price: ${total_price:.2f}'

if __name__ == '__main__':
    app.run(debug=True)
