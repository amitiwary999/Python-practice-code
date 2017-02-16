import dryscrape
from bs4 import BeautifulSoup
session=dryscrape.Session()
url='https://pythonprogramming.net/parsememcparseface/'
session.visit(url)
response=session.body()
soup=BeautifulSoup(response)
test=soup.find(id="yesnojs")
print(test.text)
