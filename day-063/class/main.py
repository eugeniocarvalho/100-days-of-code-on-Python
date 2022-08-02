# import sqlite3

# db = sqlite3.connect("books-collection.db")

# cursor = db.cursor()

# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")

# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from requests import session

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column("id", db.Integer, primary_key = True)
  title = db.Column(db.String(240), unique=True, nullable=False)
  author = db.Column(db.String(240), nullable=False)
  rating = db.Column(db.Float, nullable=False)

  def __repr__(self):
    return '<Book %r>' % self.title

db.create_all()

# new_book = Book(id=1, title="Oi", author="Bobonica", rating=9.2)
# new_book = Book(id=2, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# new_book = Book(title="Harry Potteaaaar", author="J. K. Rowling", rating=9.3)

# db.session.add(new_book)
db.session.commit()

allBooks = Book.query.all()

book2 = Book.query.filter_by(id=2).first()

book2.title = "Ilha do medo"

db.session.delete(book2)

print(book2)

db.session.commit()