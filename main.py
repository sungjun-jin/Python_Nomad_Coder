# indeed URL
# https://kr.indeed.com/jobs?q=python&limit=50&radius=25

from indeed import get_jobs as get_indeed_jobs # indeed.py 에서 extract_indeed_pages() 함수를 import

indeed_jobs = get_indeed_jobs()

print(indeed_jobs)     




