#import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#First to scrap the data from GSoC21 results, use selenium library
#to download the html file. Then use BeautifulSoup library.

url="https://summerofcode.withgoogle.com/projects"
chromedriver_path= input("Enter chromdriver_install.exe path:")
driver = webdriver.Chrome(chromedriver_path)
driver.get(url)
content = driver.page_source
soup = BeautifulSoup(content)
#page = requests.get("https://summerofcode.withgoogle.com/projects")
#soup = BeautifulSoup(page.content, 'html.parser')

#to store all the details
names=[]
projects=[]
organisations=[]

#After going through the html code of the page, got the relevant
#class id to look for, and first go thorugh all project_cards ->
#details in it, name, project, orgainsation. class id for project
#and organisation is same i.e. 'class':'md-soc-theme' ; so both
#stored in a list and then fetched. Next store them.

for entry in soup.findAll('li', attrs={'class':'project-card'}):
    person=entry.find('div', attrs={'class':'div.pos-rel'}).get_text()
    print(person)
    #detail=entry.find('div', attrs={'class':None})
    detail=entry.find('a', attrs={'class':'md-soc-theme'})
    #organisation_detail=entry.find('div',attrs={'class':})
    proj=detail[0]
    org=detail[1]
    names.append(person)
    projects.append(proj)
    organisations.append(org)

#Storing the data in the csv format
df = pd.DataFrame({'Name':names, 'Project':projects, 'Organisation':organisations})
df.to_csv('gsoc21.csv',index= False)
