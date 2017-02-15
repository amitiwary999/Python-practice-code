import requests
from bs4 import BeautifulSoup


url="http://www.makautexam.net"
r=requests.get(url)

soup=BeautifulSoup(r.content)

links=soup.find_all("a")

for link in links:
    
    print("<a href='%s'>%s</a>" %(link.get("href"),link.text))

g_data=soup.find_all("div",{"class":"modal-content formBox clearfix"})
for content in g_data:
    print(content.text)

option=soup.find_all("select",{"data-placeholder":"Choose category"})
#for item in option:
    #print(item.contents)
          
