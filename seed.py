# seed.py

from app import app, db, Book

# Create mock data
mock_books = [
    {'title': 'Atomic habits', 'author': 'James Clear'},
    {'title': 'Almanack', 'author': 'Naval Ravikant'},
    # Add more mock data as needed
]

# Create an application context
with app.app_context():
    # Seed the database
    for book_data in mock_books:
        book = Book(**book_data)
        db.session.add(book)

    # Commit the changes
    db.session.commit()

print("Database seeded successfully!")
