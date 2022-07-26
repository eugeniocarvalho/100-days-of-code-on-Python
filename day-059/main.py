from urllib import response
from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get("https://api.npoint.io/b71f3384a1c89b2a9ce5")
get_posts = response.json()

print(get_posts[0])
@app.route('/')
def home():

  return render_template('index.html', posts=get_posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/post/<id>')
def post(id):
  post = get_posts[int(id) - 1]
  print(post)
  return render_template('post.html', post=post)

if (__name__ == "__main__"):
  app.run(debug=True)