# script for scraping singer instagram handles
from bs4 import BeautifulSoup
import json

all_url_tails = []
# loop over pages
for i in range(10):
    html_file = "p" + str(i + 1) + ".htm"
    with open("singer_pages/" + html_file) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    # extract usernames
    usernames = soup.find_all("a", "kyb-ellipsis")
    url_tails = []
    for usr in usernames:
        text = usr.text
        url_tails.append(text[1:].replace(" ", "").lower() + "/")
    all_url_tails += url_tails

# create URLs
base = "https://www.instagram.com/"
direct_urls = [base + url_tail for url_tail in all_url_tails]

urls = []
for i in range(375, 500):
    print(direct_urls[i])
    urls.append(direct_urls[i])

json_res = json.dumps(urls)
with open("nash.json", "w") as f:
    f.write(json_res)

with open("nash.txt", "w") as f:
    for i in urls:
        f.write(i + "\n")
