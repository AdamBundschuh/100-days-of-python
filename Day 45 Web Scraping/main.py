from bs4 import BeautifulSoup
import lxml

with open("website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a)

anchor_tags = soup.find_all(name="a")
# print(anchor_tags)
for tag in anchor_tags:
    # print(tag.getText())
    # print(tag.get("href"))
    pass

heading = soup.find(name="h1", id="name")
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText())

company_url = soup.select_one(selector="p a") #<a> tag inside a <p> tag
company_url = soup.select_one(selector="#name") # id="name"
# print(company_url)

headings = soup.select(".heading")
# print(headings)
