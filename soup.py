import requests
from bs4 import BeautifulSoup


url="https://internshala.com/internships/matching-preferences"
r=requests.get(url)

soup=BeautifulSoup(r.content)

links=soup.find_all("a")

for link in links:
    
    print("<a href='%s'>%s</a>" %(link.get("href"),link.text))

g_data=soup.find_all("div",{"id":"form-container"})   
for content in g_data:
    print(content.contents[1].text)

option=soup.find_all("select",{"data-placeholder":"Choose category"})
#for item in option:
    #print(item.contents)
          
