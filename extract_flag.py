import requests
from bs4 import BeautifulSoup

challenge_url = "https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge"
response = requests.get(challenge_url)
soup = BeautifulSoup(response.text, "html.parser")

valid_characters = []

sections = soup.find_all("section", {"data-id": lambda x: x and x.startswith("92")})
for section in sections:
    articles = section.find_all("article", {"data-class": lambda x: x and "45" in x})
    for article in articles:
        divs = article.find_all("div", {"data-tag": lambda x: x and "78" in x})
        for div in divs:
            b_tag = div.find("b", {"class": "ref"})
            if b_tag and b_tag.has_attr("value"):
                valid_characters.append(b_tag["value"])

hidden_url = "".join(valid_characters)
print("Hidden URL:", hidden_url)
