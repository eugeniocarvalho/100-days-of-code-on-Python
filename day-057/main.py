from flask import Flask, render_template
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
  posts = Post()
  my_posts = posts.get_posts()

  return render_template("index.html", posts=my_posts)

@app.route('/blog/<num>')
def get_blog(num):
	posts = Post()
	post = posts.get_post_by_id(num)

	return render_template('post.html', post=post)

if __name__ == "__main__":
  app.run(debug=True)
