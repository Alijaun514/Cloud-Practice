from flask import Flask, render_template

app = Flask(__name__)

# Make sure this is @app.route and NOT @app.run
@app.route('/')
def home():
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": "$12.99", "img": "https://picsum.photos/200/300?random=1"},
        {"title": "1984", "author": "George Orwell", "price": "$15.50", "img": "https://picsum.photos/200/300?random=2"},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "price": "$18.00", "img": "https://picsum.photos/200/300?random=3"},
        {"title": "Atomic Habits", "author": "James Clear", "price": "$20.00", "img": "https://picsum.photos/200/300?random=4"}
    ]
    return render_template('index.html', books=books)
if __name__ == '__main__':
    # Force the host to 127.0.0.1 to avoid the 'getaddrinfo' error
    app.run(host='0.0.0.0', port=5050)