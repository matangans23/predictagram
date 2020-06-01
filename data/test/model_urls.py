import requests
from bs4 import BeautifulSoup
import json

# link with all models to scrape
models_url1 = "https://www.swaggermagazine.com/home/women/instagram-models/100-hottest-instagram-models-to-follow/"
models_url2 = "https://www.swaggermagazine.com/home/women/instagram-models/100-hottest-instagram-models-to-follow-part-2/"

# make get request & download html
r1 = requests.get(models_url1)
r2 = requests.get(models_url2)

html_doc1 = r1.text
html_doc2 = r2.text

# soup it up
soup1 = BeautifulSoup(html_doc1, 'html.parser')
soup2 = BeautifulSoup(html_doc2, 'html.parser')

# retrieve content section
content1 = soup1.find("section", "content")
content2 = soup2.find("section", "content")

# extract username <a> tags
anchors1 = content1.find_all("a")[1:51]
anchors2 = content2.find_all("a")

anchors = anchors1 + anchors2

usernames = []
# extract username <a> tags
for anchor in anchors:
    username = anchor.text[1:].replace(" ", "").lower()
    if username == "mirgaeva_galinka":
        username = "mirgaeva_galinkaofficial"
    elif username == "haileybaldwin":
        username = "haileybieber"
    elif username == "joneofthewonders":
        continue
    elif username == "mercdedesterrell":
        username = "mercedesterrell"
    username += "/"
    usernames.append(username)

# create URLs
base = "https://www.instagram.com/"
direct_urls = [base + username for username in usernames]
print(json.dumps(direct_urls))
