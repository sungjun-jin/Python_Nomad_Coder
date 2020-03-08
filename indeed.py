# indeed URL
# "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50"

import requests
from bs4 import BeautifulSoup

# 파이썬에서 요청을 만드는 기능을 모아두는 모듈

LIMIT = 50 # 한 페이지에 보여줄 구인광고 리스트의 수 
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def extract_indeed_pages() :

    result = requests.get(URL)

    soup = BeautifulSoup(result.text,'html.parser')

    pagination = soup.find("div",{"class" : "pagination"}) # <div class="pagination"> 엘리먼트 추출

    links = pagination.find_all("a") # 추출된 엘리먼트 중에서 <a> 태그 엘리먼트를 추출 


    pages = []
    for link in links[:-1] :  
        pages.append(int(link.find("span").string)) # 각 페이지의 번호를 pages list 에 옮겨담는다 

    # 가장 마지막 페이지의 번호를 max_page에 담는다 
    max_page = pages[-1] # python에서 배열의 마지막 index는 -1이다. 

    return max_page


def extract_indeed_jobs(last_page) :
    # indeed 사이트의 각 페이지 번호마다 URL을 request하기 위해 1부터 마지막 페이지인 10까지의 URL을 가져온다.
    for page in range(0,last_page) :
      
        result = requests.get(f"{URL}&start={page * LIMIT}") # 1~10 페이지의 URL을 request
        
        print(f"{page} status code = {result.status_code}") # 각 페이지의 status code를 출력


extract_indeed_jobs(extract_indeed_pages())



