from crypt import methods
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
Bootstrap(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


@app.route('/')
def home():
    all_books = Book.query.all()

    return render_template("index.html", books=all_books)

db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column("id", db.Integer, primary_key = True)
  title = db.Column(db.String(240), unique=True, nullable=False)
  author = db.Column(db.String(240), nullable=False)
  rating = db.Column(db.Float, nullable=False)

db.create_all()

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("home"))

    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        book_id = request.form["id"]
        print(book_id)
        book_to_update = Book.query.filter_by(id=book_id).first()
        book_to_update.rating = request.form["rating"]

        db.session.commit()
        
        return redirect(url_for('home'))
    
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get("id")

    book = Book.query.filter_by(id=book_id).first()

    db.session.delete(book)
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

