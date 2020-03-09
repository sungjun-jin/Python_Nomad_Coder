# stackoverflow URL
# https://stackoverflow.com/jobs?q=python
# https://stackoverflow.com/jobs?q=python&pg=2

import requests
from bs4 import BeautifulSoup

URL = "https://stackoverflow.com/jobs?q=python"
MAX_PAGE = 9


def extract_stackoverflow_pages() :

    #for page in range(0,MAX_PAGE) :

        result = requests.get(f"{URL}&pg={2}")
        print(f"{URL}&pg={2}")         
        soup = BeautifulSoup(result.text,"html.parser")        
        results = soup.find("a",{"class" : "s-link stretched-link"})

        extract_jobs(results.string) 
    



def extract_jobs(html) :
       
    print(html)

    
    

extract_stackoverflow_pages() 