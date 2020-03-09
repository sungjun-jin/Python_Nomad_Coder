import csv

def save_to_file(jobs) :
    
    #파일 생성
    file = open("jobs.csv", mode = "w", encoding='UTF-8',newline='') # mode = w -> 쓰기만 설정, newline 문자 처리 

    #csv를 작성해주는 writer 생성 
    writer = csv.writer(file)

    writer.writerow(["Title", "Company", "Location"])
    for job in jobs :
        writer.writerow(list(job.values()))

    print(file)
    return 

