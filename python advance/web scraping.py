import  requests
from bs4 import BeautifulSoup
r=requests.get("https://google.com")
c=r.content
soup=BeautifulSoup(c,"html.parser")
print(soup.prettify())

