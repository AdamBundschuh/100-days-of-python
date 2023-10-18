from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

article_text = []
article_links = []
article_upvotes = []

articles = soup.select(".titleline > a")
for article in articles:
    article_text.append(article.getText())

    if article.get("href").startswith("item?id="):
        article_link = "https://news.ycombinator.com/" + article.get("href")
        article_links.append(article_link)
    else:
        article_links.append(article.get("href"))

for td in soup.find_all(name="td", class_="subtext"):
    score_span = td.find(name="span", class_="score")
    if score_span is not None:
        article_upvotes.append(int(score_span.getText().split()[0]))
    else:
        article_upvotes.append(0)

high_score = max(article_upvotes)
hs_index = article_upvotes.index(high_score)

print("Most upvoted article from Hacker News:")
print(f"Title: {article_text[hs_index]}")
print(f"Link: {article_links[hs_index]}")
print(f"Score: {article_upvotes[hs_index]}")
