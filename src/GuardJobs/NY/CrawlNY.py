from src.GuardJobs.Website import Website
from src.GuardJobs.Crawler import Crawler
from src.GuardJobs.AGRJob import AGRJob
from bs4 import BeautifulSoup


class NyWebsite(Website):
    TABLE_SELECTOR = 'jobnavtable'
    NAME = "DMNA"
    URL = 'https://dmna.ny.gov/jobs/'
    TECHURL = 'https://dmna.ny.gov/jobs/?id=tech'
    AGRURL = 'https://dmna.ny.gov/jobs/?id=agr'

    def __init__(self):
        super().__init__(self.URL, self.NAME, self.TECHURL, self.AGRURL)


class NyCrawler(Crawler):

    REGION = ['NATIONWIDE', 'STATEWIDE', 'ON BOARD']
    JOBTABLECLASS = '.jobtable'

    def __init__(self, website):
        self.crawl(website)

    def getUsaJobsData(self, url):
        """Information on Technician jobs is located on usajobs.com. This function pulls data from it

        Args:
            url (string): direct link to a specific Technician job posting
        """
        usa_bs = self.getPage(url)
        if (usa_bs != None):
            pTags = usa_bs.select('p')
            for tag in pTags:
                if 'Military Grades: ' in tag.text:
                    print(tag.text)

    def processDmnaTechJobsData(self, jobList):
        """transform blob of text returned from DMNA website job table crawl, associates data with USAJOBS link
            ARGS:
                jobList (list): bs4 resultset with rows (bs4.element.tag objects) from DMNA job table
            Returns:
                dictionary: Jobs data keyed by job id
        """
        for index in range(1, len(jobList)):  # cut off header row
            html = jobList[index]
            usaJobsurl = html.select('a')[0].get('href')
            # NATIONWIDE, STATEWIDE, ON BOARD
            adRange = html.select('p')[0].get_text()
            cells = html.select('td')
            id = cells[0].get_text()
            title = cells[1].get_text().replace('NATIONWIDE', '').replace(
                'STATEWIDE', '').replace('ON BOARD', '')
            tech_grade = cells[2].get_text()
            location = cells[4].get_text()
            closeDate = cells[5].get_text()
            usaJobsData = self.getUsaJobsData(usaJobsurl)
            # agr = AGRJob(title, adRange,)
            # print(title, adRange, id)

    def getTechJobs(self, techPageBS):
        jobList = techPageBS.select(self.JOBTABLECLASS)[0].select('tr')
        if (len(jobList) > 0):
            self.processDmnaTechJobsData(jobList)
        else:
            raise Exception('NY: No Technician data returned')

    def getAgrJobs(self):
        return {}

    def crawl(self, website):
        techPageBS = self.getPage(website.TECHURL)
        agrPageBS = self.getPage(website.AGRURL)
        self.techDict = self.getTechJobs(techPageBS)
        # self.agrDict = self.getAgrJobs(agrPage)


def getCrawler():
    website = NyWebsite()

    return NyCrawler(website)
