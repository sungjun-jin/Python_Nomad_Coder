# indeed URL
# https://kr.indeed.com/jobs?q=python&limit=50&radius=25

from indeed import extract_indeed_pages # indeed.py 에서 extract_indeed_pages() 함수를 import


max_indeed_pages = extract_indeed_pages()

for n in range(max_indeed_pages) :

    print(f"start={n * 50}") # python f print문 연습하기
        

     


