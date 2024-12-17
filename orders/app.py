# Order Service
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

orders = {}

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(list(orders.values())), 200

@app.route('/orders', methods=['POST'])
def place_order():
    data = request.json
    order_id = str(uuid4())
    order = {"id": order_id, **data}
    orders[order_id] = order
    return jsonify(order), 201

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200

if __name__ == "__main__":
    app.run(port=5001)