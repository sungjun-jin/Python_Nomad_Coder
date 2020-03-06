# indeed URL
# https://kr.indeed.com/jobs?q=python&limit=50&radius=25

import requests
from bs4 import BeautifulSoup

# 파이썬에서 요청을 만드는 기능을 모아두는 모듈

INDEED_URL = "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50"
LIMIT = 50

def extract_indeed_pages() :

    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text,'html.parser')

    pagination = soup.find("div",{"class" : "pagination"})

    links = pagination.find_all("a")


    pages = []
    for link in links[:-1] :  
        pages.append(int(link.find("span").string))

    max_page = pages[-1]

    return max_page


def extract_indeed_jobs(last_page) :

    for page in range(0,last_page) :

        print(f"{INDEED_URL}&start={page * 50}") 


extract_indeed_jobs(extract_indeed_pages())



