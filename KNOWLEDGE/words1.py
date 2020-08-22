from bs4 import BeautifulSoup as soup 
from urllib.request import urlopen 
from urllib.request import Request

url = "https://gre.economist.com/gre-advice/gre-vocabulary/which-words-study/most-common-gre-vocabulary-list-organized-difficulty"

req = Request(url)
page_html = urlopen(req).read()
page_soup = soup(page_html,"html.parser")

ps = page_soup.find_all("p")
# pss = ps.find("p")
texxt = ps[3].text
# print(pss)
lsst = texxt.split('The Economist')
nlsst = []
for i in lsst:
    i = i.split('Synonyms:',1)
    i.extend(i[1].split('Source:',1))
    i.remove(i[1])
    i[1] = 'Synonyms:' + i[1]
    i[2] ='Source:' + i[2] + 'The Economist'
    nlsst.append("\n".join(i))
    print(nlsst[0])

print(nlsst[300])
lsst = nlsst
# print(lsst[0])
# for i in 