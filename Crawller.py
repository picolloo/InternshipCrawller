import Job
import requests
from bs4 import BeautifulSoup

class Crawller:
    def __init__(self):
        self.url_base = 'https://estagios.ufsc.br/index.php?page=search&cursos[]='

    def dig(self, _course):
        jobs = []
        url_r = requests.get(self.url_base + str(_course))

        enconding = url_r.encoding if 'charset' in url_r.headers.get('content-type', '').lower() else None

        if url_r.status_code == 200:
            url_soup = BeautifulSoup(url_r.content, 'html.parser', from_encoding=enconding)
            tbody = url_soup.find('tbody')
            jobOffers = tbody.findChildren('td')
            for job in jobOffers:
                link = job.find('a', href=True)['href']
                url_offer_r = requests.get(link)

                if url_offer_r.status_code == 200:
                    job_s = BeautifulSoup(url_offer_r.content, 'html.parser')

                    divHead = job_s.find(id='item_head')
                    if divHead:
                        jobTitle = divHead.findChild('strong').text
                    else:
                        jobTitle = "Not defined"

                    divDates = job_s.find(id='type_dates')
                    if divDates:
                        jobType = divDates.findChild('strong').text
                        dates = divDates.findAll('em')
                        jobPublishment = dates[0].text
                        jobExpire = dates[1].text
                    else:
                        jobType = "Not defined"
                        jobPublishment = "Not defined"
                        jobExpire = "Not defined"

                    #---IMPLEMENT MAPS
                    divLocation = job_s.find(id='item_location').find('strong')
                    if divLocation:
                        jobAddress = divLocation.text
                    else:
                        jobAddress = "Not defined"

                    description = job_s.find(id='description').find('p').text

                    divImgs = job_s.find(id='description').findChildren('img')

                    infos = []
                    for count in range (3):
                        infos.append(divImgs[count].get('alt',''))


                    jobs.append(Job.Job(link, jobTitle, jobType, jobPublishment, jobExpire, jobAddress, description, infos))

        return jobs

crawller = Crawller()
for job in crawller.dig(238):
    print('--------------------------------------')
    print('URL: ', job.url)
    print('Title: ', job.title)
    print('Type: ', job.type)
    print('Publish: ', job.publishment)
    print('Expire: ', job.expire)
    print('Address: ', job.address)
    print('Desc: ', job.description)
    print('Info[0]: ', job.info[0])
    print('Info[1]: ', job.info[1])
    print('Info[2]: ', job.info[2])
    print('--------------------------------------')


