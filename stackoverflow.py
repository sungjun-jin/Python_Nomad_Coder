# stackoverflow URL
# https://stackoverflow.com/jobs?q=python
# https://stackoverflow.com/jobs?q=python&pg=2

import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python&sort=i"
    

def get_last_page() :
    result = requests.get(URL)
    soup = BeautifulSoup(result.text,'html.parser')

    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")   

    last_page = pages[-2].get_text(strip=True)

    return int(last_page)


def extract_jobs(last_page) :

    jobs = []
    
    
    for page in range(5) :
        result = requests.get(f"{URL}&pg={page+1}") # 0 부터 시작하므로 
        print(f"printing stackoverflow page : {page+1}")
        soup = BeautifulSoup(result.text,"html.parser")        
        results = soup.find_all("div",{"class":"-job"})

        for result in results :
            job = extract_job(result)
            jobs.append(job)   


    return jobs    

def extract_job(html) :
        
        # 직무
        title = html.find("h2",{"class":"mb4 fc-black-800 fs-body3"}).find("a")["title"]

        # 회사
        company =   html.find("h3",{"class": "fc-black-700 fs-body1 mb4"}).find("span").get_text(strip=True) # 공백 제거 

        # 주소  
        
        location = html.find("span",{"class":"fc-black-500"}).get_text(strip=True)        
        
        #title,company,location으로 구성된 dictionary 반환
        return {
            "title":title,
            "company":company,
            "location":location
            }

    

def get_jobs() :
    last_page = get_last_page()
    jobs = extract_jobs(last_page)
    return jobs


get_jobs()