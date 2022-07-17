import requests

class Post:
    def __init__(self):
      response = requests.get("https://api.npoint.io/b71f3384a1c89b2a9ce5")
      self.posts = response.json()

    def get_posts(self):
      return self.posts
    
    def get_post_by_id(self, id):
      return self.posts[int(id) - 1]

      