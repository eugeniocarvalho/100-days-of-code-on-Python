from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(".titlelink")
articles_upvotes = []
rows = soup.find_all(name="td", class_="subtext")
articles_link = []
articles_text = []

for row in rows:
  score = row.find(name="span", class_="score")
  
  if score == None:
    score = 0
  else:
    score = int(score.getText().split(" ")[0])

  articles_upvotes.append(score)

for article in articles:
  articles_text.append(article.getText())
  articles_link.append(article.get("href"))

max_score = articles_upvotes.index(max(articles_upvotes))
print(max_score)
print(articles_text[max_score])
print(articles_link[max_score])
print(articles_upvotes[max_score])
