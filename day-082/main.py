from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-boboniqued'

Bootstrap(app)


@app.route('/')
def home():
  return render_template('index.html')


@app.route('/hire-me')
def hire_me():
  return render_template('hire-me.html')


if __name__ == "__main__":
  app.run(debug=True)