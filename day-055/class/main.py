from flask import Flask

app = Flask(__name__)

def make_bold(function):
  def wrapper_function():
    text = function()
    return f"<strong>{text}</strong>"
  return wrapper_function

def make_underlined(function):
  def wrapper_function():
    text = function()
    return f"<u>{text}</u>"
  return wrapper_function

@app.route('/')
def opa():
  return '<p>Opa meu amigo</p>'

@app.route('/bye')
@make_bold
@make_underlined
def bye():
  return 'Bye!'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
  return f"<h1 style='text-align: center;'>Opa, {name}, seja bem vindo! Tu tem {number} anos?</h1><p>Diga sim ou não.</p>"


if __name__ == "__main__":
  app.run(debug=True)