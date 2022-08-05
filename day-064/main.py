from crypt import methods
from hashlib import new
from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from h11 import Data
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests, os

TMDB = os.getenv("TMDB")
URL = f"https://api.themoviedb.org/3/search/movie"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"

Bootstrap(app)

db = SQLAlchemy(app)

class Movie(db.Model):
  id = db.Column(db.Integer, unique=True, primary_key=True)
  title = db.Column(db.String(250), unique=True, nullable=False)
  year = db.Column(db.Integer, nullable=False)
  description = db.Column(db.String(250), nullable=False)
  rating = db.Column(db.Float, nullable=True)
  ranking = db.Column(db.Integer, nullable=True)
  review = db.Column(db.String(250), nullable=True)
  img_url = db.Column(db.Text, nullable=False)

db.create_all()

class AddForm(FlaskForm):
  title = StringField("Movie title: ", validators=[DataRequired()])
  submit = SubmitField("Add Movie")

class EditForm(FlaskForm):
  rating = StringField('Rating:', validators=[DataRequired()])
  review = StringField('Your Review:', validators=[DataRequired()])
  submit = SubmitField('Done')

@app.route("/")
def home():
  all_movies = Movie.query.all()

  for i in range(len(all_movies)):
    all_movies[i].ranking = len(all_movies) - i

  return render_template("index.html", movies=all_movies)

@app.route("/edit", methods=["GET", "POST"])
def edit():
  form = EditForm()
  movie_id = request.args.get("id")
  movie_update = Movie.query.get(movie_id)
  movie_title = movie_update.title

  print(movie_update.rating)

  if form.validate_on_submit():
    rating = float(form.rating.data)
    review = form.review.data
    movie_update.rating = rating
    movie_update.review = review
    db.session.commit()

    return redirect(url_for('home'))

  return render_template('edit.html', form=form, movie=movie_update)

@app.route("/delete", methods=["GET", "POST"])
def delete():
  movie_id = request.args.get("id")

  movie = Movie.query.get(movie_id)

  db.session.delete(movie)
  db.session.commit()

  return render_template('index.html')

@app.route("/add", methods=["GET", "POST"])
def add():
  form = AddForm()
  
  if form.validate_on_submit():
    response = requests.get(URL, params={"api_key": TMDB, "query": form.title.data}).json()["results"]

    return render_template('select.html', movies=response)

  return render_template('add.html', form=form)

@app.route("/find")
def find_movie():
  movie_api_id = request.args.get("id")

  if movie_api_id:
    movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"

    response = requests.get(movie_api_url, params={"api_key": TMDB, "language": "en-US"}).json()

    new_movie = Movie(
      title = response["title"],
      year = response["release_date"].split("-")[0],
      img_url = f"{MOVIE_DB_IMAGE_URL}{response['poster_path']}",
      description = response["overview"],
      rating = 0.0,
      review = " "
    )

    db.session.add(new_movie)
    db.session.commit()
    
    return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
  app.run(debug=True)
