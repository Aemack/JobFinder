import requests
import random
from bs4 import BeautifulSoup

def getTotalJobs(title, location):
    #https://www.totaljobs.com/jobs/front-end-developer/in-edinburgh
    URL = 'https://www.totaljobs.com/jobs/'
    titleArray = title.split()
    for word in titleArray:
        URL = URL + word +'-'
    URL = URL + '/in-'
    locationArray = location.split()
    for word in locationArray:
        URL = URL + word +'-'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div',{'class':'job'})
    resultArray = []
    for result in results:
        resultObject = {}
        resultObject['title'] = result.find('div',{'class':'job-title'}).text.replace('\n','').replace('\r','')
        resultObject['posted_by'] = result.find('li',{'class':'company'}).text.replace('\n','').replace('\r','')
        resultObject['salary'] = result.find('li',{'class':'salary'}).text.replace('\n','').replace('\r','')
        resultObject['link'] = result.find('a',{'class':'btn-seejob'})['href']
        resultObject['taken_from'] = "Total"

        resultArray.append(resultObject)

    return resultArray

def getMonsterJobs(title, location):
    URL = 'https://www.monster.co.uk/jobs/search/?q='
    titleArray = title.split()
    for word in titleArray:
        URL = URL + word +'-'
    URL = URL + '&where='
    locationArray = location.split()
    for word in locationArray:
        URL = URL + word +'-'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div',{'class':'summary'})

    resultArray = []
    for result in results:
        try:
            resultObject = {}
            resultObject['title'] = result.find('h2',{'class':'title'}).text.replace('\n','').replace('\r','')
            resultObject['posted_by'] = result.find('div',{'class':'company'}).text.replace('\n','').replace('\r','')
            resultObject['link'] = result.select('h2[class = "title"] a')[0]['href']
            resultObject['taken_from'] = "Monster"
        except:
            print('error')
        else:
            resultArray.append(resultObject)
    return resultArray

def getReedJobs(title,location):
    URL = 'https://www.reed.co.uk/jobs/'
    titleArray = title.split()
    for word in titleArray:
        URL = URL + word +'-'
    URL = URL + '-in-'
    locationArray = location.split()
    for word in locationArray:
        URL = URL + word +'-'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('article',{'class':'job-result'})


    resultArray = []
    for job_elem in results:
        resultObject = {}
        title = job_elem.find('h3', class_='title')
        link = job_elem.find('a', class_='gtmJobTitleClickResponsive')
        posted_by = job_elem.find('a', class_='gtmJobListingPostedBy')
        salary = job_elem.find('li', class_='salary')
        resultObject['taken_from'] = "Reed"

        resultObject['title'] = title.text.replace("\n","")
        resultObject['posted_by'] = posted_by.text
        resultObject['salary'] = salary.text
        if link != None:
            resultObject['link'] = "https://www.reed.co.uk/"+link['href']
        else:
            resultObject['link'] = "https://www.reed.co.uk/"
        resultArray.append(resultObject)

    return resultArray


def getJobs(title, location):
    jobArray = []
    jobArray += getMonsterJobs(title, location)
    jobArray += getReedJobs(title, location)
    jobArray += getTotalJobs(title, location)

    return jobArray

def main(title, location):
    jobObject = getJobs(title, location)

    random.shuffle(jobObject)

    return jobObject
