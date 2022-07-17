from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
  random_number = random.randint(1, 10)
  current_year = datetime.today().year
  return render_template('index.html', number=random_number, year=current_year)

@app.route('/guess/<name>')
def guess_name(name):
  response = requests.get(f'https://api.genderize.io/?name={name}').json()
  person_gender = response["gender"]

  response = requests.get(f"https://api.agify.io/?name={name}").json()
  person_age = response["age"]

  return render_template('guess.html', name=name, gender=person_gender, age=person_age)

@app.route('/blog/<num>')
def get_blog(num):
  blog_url = "https://api.npoint.io/b71f3384a1c89b2a9ce5"

  response = requests.get(blog_url)

  all_posts = response.json()

  return render_template('blog.html', posts=all_posts, blog_number=num)

if __name__ == "__main__":
  app.run(debug=True) 