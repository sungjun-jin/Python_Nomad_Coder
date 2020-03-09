# indeed URL
# "https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit=50"

import requests
from bs4 import BeautifulSoup

# 파이썬에서 요청을 만드는 기능을 모아두는 모듈

LIMIT = 50 # 한 페이지에 보여줄 구인광고 리스트의 수 
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?q=python&limit={LIMIT}"


def get_last_page() :

    #indeed job search 결과의 마지막 페이지를 리턴해주는 함수 

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


def extract_jobs(last_page) :
    # indeed 사이트의 각 페이지 번호마다 URL을 request하기 위해 1부터 마지막 페이지인 10까지의 URL을 가져온다.
    jobs = []
    for page in range(0,last_page) :
        
        print(f"scraping page = {page}")
        result = requests.get(f"{URL}&start={page * LIMIT}") # 1~10 페이지의 URL을 request       
        soup = BeautifulSoup(result.text,"html.parser") #soup를 만들어 데이터를 추출 
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
    

    for result in results :
        job = extract_job(result)
        jobs.append(job)
          

    return jobs            
 
        

def extract_job(html) :

    # title : 직무
    # company : 회사 
    
    #직무 추출하기 
    title = html.find("div",{"class": "title"}) # <div class="title"> 인 요소만 추출하는 soup
    title = title.find("a")["title"] # 속성(attribute)으로 추출하는 방법 : soup.find()["속성이름"], 한 줄로도 만들 수 있지만 익숙해질때까진 두 줄로 코딩하자 
    
        
    #회사 추출하기
    company = html.find("span",{"class": "company"}) # company soup 생성
    # 링크 (anchor)가 있는 회사도 있고 없는 회사도 있으므로 anchor 태그 유무에 따라 분기처리를 해준다. 
    company_anchor = company.find("a")        
    if company_anchor is not None: 
        company = str(company_anchor.string) # 원래 company 변수는 위에서 soup 였지만 string형으로 재할당이 가능하다.
    else :
        company = str(company.string) 
    company = company.strip() # strip()은 문자열 양끝에 있는 공백을 지워준다

    #위치 추출하기

    #indeed 사이트에서 위치정보를 담고있는 태그는 div태그와 span태그 2개다.
    #따라서 분기처리를 해준다     
    location = ""
    location_span =  html.find("span",{"class" : "location accessible-contrast-color-location"})

    if location_span is not None :
        location = location_span.string
    else :
        location_div = html.find("div",{"class" : "location accessible-contrast-color-location"})
        location = location_div.string

    # https://kr.indeed.com/jobs?q=python&limit=50&advn=2377738824512678&vjk=c1037225077ca4da
    #job_id 추출
    #job_id = html["data-jk"]      

    # dictionary를 return 해준다.
    return {"title" : title, 
    "company" : company, 
    "location" : location,     
    }

def get_jobs() :

    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs          