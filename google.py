import requests,bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

class Google:
	def __init__(self):
		self.count = 0
		
	def search(self,url):
		url = parser(ses.get(url).text,"html.parser")
		for z in url.find_all("a",{"href":True}):
			if "/url?q=" in z["href"]:
				if "google.com" in z["href"]:
					pass
				else:
					self.count += 1
					print(f" {self.count}. {z.text} -> {z['href']}")
		for x in url.find_all("a",{"href":True}):
			if "Berikutnya >" in x.text:
				self.search("https://www.google.com"+x["href"])
	
Google().search("https://www.google.com/search?q=indonesia")