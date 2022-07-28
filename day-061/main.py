from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators, EmailField
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
  email = EmailField('Email: ', [validators.DataRequired(message="Please enter your email address."), validators.Email()])
  password = PasswordField('Password: ', [validators.DataRequired(), validators.Length(8)])

  submit = SubmitField('Submit')

app = Flask(__name__)
app.secret_key = "giripupu-meu-amig"
Bootstrap(app)

@app.route("/")
def home():
  return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  login_form = LoginForm()
  if login_form.validate_on_submit():
    email = login_form.email.data
    password = login_form.password.data

    if email == 'admin@email.com' and password == '12345678':
      return render_template('success.html')
    else:
      return render_template('denied.html')
  return render_template('login.html', form=login_form)

if __name__ == '__main__':
  app.run(debug=True)