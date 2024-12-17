# Catalog Service
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

books = {}

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(list(books.values())), 200

@app.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book_id = str(uuid4())
    book = {"id": book_id, **data}
    books[book_id] = book
    return jsonify(book), 201

@app.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    return jsonify(book), 200

if __name__ == "__main__":
    app.run(port=5000)
