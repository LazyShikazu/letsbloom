# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)

# Endpoint 1: Retrieve All Books
@app.route('/api/books', methods=['GET'])
def get_all_books():
    try:
        books = Book.query.all()
        book_list = []
        for book in books:
            book_list.append({'id': book.id, 'title': book.title, 'author': book.author})
        return jsonify({'books': book_list})
    
    except SQLAlchemyError as e:
        # Handle specific database-related errors
        db.session.rollback()  # Rollback the transaction
        return jsonify({'error': 'Database connection issue'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint 2: Add a New Book
@app.route('/api/books', methods=['POST'])
def add_new_book():
    try:
        data = request.get_json()
        
        # Validate request payload
        if not data or 'title' not in data or 'author' not in data:
            return jsonify({'error': 'Invalid request payload'}), 400

        # Check for duplicate book entries
        existing_book = Book.query.filter_by(title=data['title']).first()
        if existing_book:
            return jsonify({'error': 'Book with the same title already exists'}), 409  # 409 Conflict

        
        new_book = Book(title=data['title'], author=data['author'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Endpoint 3: Update Book Details
@app.route('/api/books/<int:id>', methods=['PUT'])
def update_book_details(id):
    try:
        
        # # Validate request payload
        # if not data or ('title' not in data and 'author' not in data):
        #     return jsonify({'error': 'Invalid request payload'}), 400
        
        book = Book.query.get(id)
        if book:
            data = request.get_json()
            book.title = data.get('title', book.title)
            book.author = data.get('author', book.author)
            db.session.commit()
            return jsonify({'message': 'Book updated successfully'})
        else:
            return jsonify({'error': 'Book not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
# Endpoint 4: Delete a Book
@app.route('/api/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    try:
        book = Book.query.get(id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return jsonify({'message': 'Book deleted successfully'})
        else:
            return jsonify({'error': 'Book not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Create an application context before calling db.create_all()
with app.app_context():
    # Create tables in the database
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
