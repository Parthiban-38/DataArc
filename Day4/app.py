from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory book store
books = []

# Home route for testing (optional)
@app.route('/')
def home():
  return render_template('index.html')

# @app.route('/books')
# def book_page():
#     return render_template('index.html')
# 📘 Get all books
@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify({'books': books}), 200

# 📘 Add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    data = request.json  # expecting JSON data
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({'error': 'Title and author are required'}), 400
    
    book = {
        'title': data['title'],
        'author': data['author']
    }
    books.append(book)
    return jsonify({'message': 'Book added', 'book': book}), 201

if __name__ == '__main__':
    app.run(debug=True)
