from bs4 import BeautifulSoup
import requests
import re

data = {}

link = 'https://www.worldtimeserver.com/current_time_in_US-FL.aspx'
r = requests.get(link)
soup = BeautifulSoup(r.content, 'lxml')
time_data = soup.find("span",{"class": "fontTS"}).get_text()
date_data = soup.find("span",{"class": "font6"}).get_text()
time_data = time_data.replace(" ","")
time_data = time_data.replace("\n","")
date_data = date_data.replace(" ","")
date_data = date_data.replace("\n","")
data["time"] = time_data
data["date"] = date_data
print(data["time"]+"\n"+data["date"])
