from crypt import methods
from urllib import response
from flask import Flask, render_template, request
import requests, os, smtplib
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PERSONAL_EMAIL = os.getenv("PERSONAL_EMAIL")

response = requests.get("https://api.npoint.io/b71f3384a1c89b2a9ce5")
get_posts = response.json()

@app.route('/')
def home():

  return render_template('index.html', posts=get_posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  title = "Contact Me"
  return render_template('contact.html', title=title)

@app.route('/form-entry', methods=["GET", "POST"])
def recieve_data():
  if request.method == "POST":
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    print(name)
    print(email)
    print(phone)
    print(message)

    title = "Successfully sent your message"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
      connection.starttls()
      connection.login(user=EMAIL, password=PASSWORD)
      message = f"Subject:Contact Blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}"

      connection.sendmail(
        from_addr=EMAIL,
        to_addrs= PERSONAL_EMAIL,
        msg=message
      )

    return render_template('contact.html', title=title)
  elif request.method == "GET":
    title = "Contact Me"

    return render_template('contact.html', title=title)

@app.route('/post/<id>')
def post(id):
  post = get_posts[int(id) - 1]

  return render_template('post.html', post=post)

if (__name__ == "__main__"):
  app.run(debug=True)