import requests
from bs4 import BeautifulSoup

def text(x):
    return x.get_text()

url = "https://www.theglobeandmail.com/world/"
globeAndMailRequest = requests.get(url)
homepageContent = globeAndMailRequest.content

parsed = BeautifulSoup(homepageContent, 'html5lib')
anchorLinks = parsed.find_all('a', class_="c-card__grid c-card__link")

articleLinks = []
for i in range(5):
    articleLinks.append(anchorLinks[i]['href'][7::])

articleText = []

for i in articleLinks:
    articleRequest = requests.get(url + i)
    #print(url+i)
    articleContent = articleRequest.content
    articleParsed = BeautifulSoup(articleContent, 'html5lib')
    anchorLinks = articleParsed.find_all('p', class_="c-article-body__text")
    print(articleContent)
    articleText.append(anchorLinks)

print(articleText)