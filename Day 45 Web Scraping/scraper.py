from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")

article_text = []
article_links = []

# BUG: HTML of the Hacker News site has been updated since the course
# Using the '>' character in the selector will only select 'a' tags that are a direct child of the .titleline class
# This prevents the 'a' tags from being counted that appear at the end of the article in the parenthesis
articles = soup.select(".titleline > a")
for article in articles:
    article_text.append(article.getText())

    # BUG: Some articles link directly to a Hacker News story, and only provide the internal ID
    # In this case, we append the ycombinator URL in front of it
    if article.get("href").startswith("item?id="):
        article_link = "https://news.ycombinator.com/" + article.get("href")
        article_links.append(article_link)
    else:
        article_links.append(article.get("href"))

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# BUG: If an article has no upvotes, nothing is added to the article_upvotes list
# This causes the indexes to be out of sync
# First we find all the <td> with the class of 'subtext' (This returns the row directly below the article title)
# We loop through the <td> items, and if it contains another nested <td> with the class of 'score'
# then we strip out the number. Otherwise, if it does not find a <td> with a class of 'score' then there are no
# upvotes for that article, and we add a zero to the article_upvotes list, keeping the index accurate.

article_upvotes = []

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
