from bs4 import BeautifulSoup
import requests
import time

print('Enter your minimum salary requirement:')
min_salary = input('>>>>')
print(f'Filtering jobs paying less than {min_salary}')

def find_python_dev_jobs():
    html_text = requests.get('https://www.reed.co.uk/jobs/python-developer-jobs-in-london').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('div', class_='col-sm-12 col-md-7 col-lg-8 col-xl-9')
    #print(job)
    for index, job in enumerate(jobs):   
        posting_date = job.find('div', class_ = 'job-card_jobResultHeading__postedBy__sK_25').text
        if 'days ago' in posting_date: 
            job_info = job.find_all('li')
            salary = job_info[0].text
            if int(salary.split()[2][1:].replace(',', '')) >= int(min_salary):
                job_title = job.find('h2', class_ = 'job-card_jobResultHeading__title__IQ8iT').text
                more_info = job.header.h2.a['href']
                location = job_info[1].text
                job_time = job_info[-1].text

                with open(f'Posted jobs/{index}.txt', 'w') as f:
                    f.write(f'Job title: {job_title}\n')
                    f.write(f'Salary: {salary}\n')
                    f.write(f'Location: {location}\n')
                    f.write(f'Contract/hours: {job_time}\n')
                    f.write(f'More info: https://www.reed.co.uk{more_info}')
                print(f'Matching job file created {index}')
if __name__ == "__main__":
    while True:
        find_python_dev_jobs()
        wait_time = 15
        print(f'Waiting {wait_time}mins before rerunning.')
        time.sleep(wait_time * 60)