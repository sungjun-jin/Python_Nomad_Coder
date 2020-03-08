# indeed URL
# https://kr.indeed.com/jobs?q=python&limit=50&radius=25

from indeed import extract_indeed_pages, extract_indeed_jobs # indeed.py 에서 extract_indeed_pages() 함수를 import


last_indeed_page = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_page) 


     




