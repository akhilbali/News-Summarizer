import requests
from bs4 import BeautifulSoup

class Extract:

	def __init__(self,url):
		self.url=url

	def get_data(self):
		html_code = requests.get(self.url,verify=False)
		soup=BeautifulSoup(html_code.text,"lxml")
		article=""
		for para in soup.findAll('p',{'class':'story-body-text story-content'}):
			article=article+para.text+"\n"
		return (article)
