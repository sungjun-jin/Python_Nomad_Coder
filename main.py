# indeed URL
# https://kr.indeed.com/jobs?q=python&limit=50&radius=25

from indeed import get_jobs as get_indeed_jobs # indeed.py 에서 extract_indeed_pages() 함수를 import
from stackoverflow import get_jobs as get_so_jobs # stackoverflow.py 에서 extract_indeed_pages() 함수를 import
from save import save_to_file


# so_jobs = get_so_jobs()
indeed_jobs = get_indeed_jobs()
so_jobs = get_so_jobs()
jobs = indeed_jobs + so_jobs
save_to_file(jobs)



 




