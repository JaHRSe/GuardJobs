from src.GuardJobs.Website import Website
from src.GuardJobs.Crawler import Crawler
from src.GuardJobs.AGRJob import AGRJob
from src.GuardJobs.Civjob import CivJob
from bs4 import BeautifulSoup


class NyWebsite(Website):
    TABLE_SELECTOR = 'jobnavtable'
    NAME = "DMNA"
    URL = 'https://dmna.ny.gov/jobs/'
    CIVURL = 'https://dmna.ny.gov/jobs/?id=tech'
    AGRURL = 'https://dmna.ny.gov/jobs/?id=agr'

    def __init__(self):
        super().__init__(self.URL, self.NAME, self.CIVURL, self.AGRURL)


class NyCrawler(Crawler):

    REGION = ['NATIONWIDE', 'STATEWIDE', 'ON BOARD']
    JOBTABLECLASS = '.jobtable'

    def __init__(self, website):
        self.crawl(website)
        self.civ_job_list = []
        self.agr_list = []

    def get_usa_jobs_data(self, url):
        """Information on Technician jobs is located on usajobs.com. This function pulls data from it

        Args:
            url (string): direct link to a specific Technician job posting
        """
        military_grade = None
        usa_bs = self.get_page(url)
        if (usa_bs != None):
            pTags = usa_bs.select('p')
            for tag in pTags:
                if 'Military Grades: ' in tag.text:
                    if 'officer' in tag.text.lower():
                        military_grade = 'Officer'
                    else:
                        military_grade = 'Enlisted'
        return ({
            'military_grade': military_grade
        })

    def process_civ_data(self, job_list):
        """transform blob of text returned from DMNA website job table crawl, associates data with USAJOBS link
            ARGS:
                jobList (BeutifulSoup[]): bs4 resultset with rows (bs4.element.tag objects) from DMNA job table
            Returns:
                [CivJob Objects] 
        """
        civ_jobs = []
        for index in range(1, len(job_list)):  # cut off header row
            html = job_list[index]
            usa_url = html.select('a')[0].get('href')
            usa_jobs_data = self.get_usa_jobs_data(usa_url)
            # NATIONWIDE, STATEWIDE, ON BOARD
            ad_range = html.select('p')[0].get_text()
            cells = html.select('td')
            id = cells[0].get_text()
            pos_title = cells[1].get_text().replace('NATIONWIDE', '').replace(
                'STATEWIDE', '').replace('ON BOARD', '')
            civ_grade = cells[2].get_text()
            code_title = cells[3].get_text()
            location = cells[4].get_text()
            close = cells[5].get_text()
            civ_jobs.append(CivJob(
                id=id,
                pos_title=pos_title,
                code_title=code_title,
                military_grade=usa_jobs_data['military_grade'],
                ad_range=ad_range,
                civ_grade=civ_grade,
                location=location,
                close=close,
            ))
        return civ_jobs

    def process_agr_data(self, job_list):
        """Scrapes AGR job postings on DMNA website

        Args:
            jobList (BeutifulSoup[]): bs4 resultset with rows (bs4.element.tag objects) from DMNA AGR job table
        Returns: 
            [Agrjob Objects]
        """
        agr_jobs = []
        for index in range(1, len(job_list)):  # cut off header row
            html = job_list[index]
            # check if cancelled
            cancelled = bool(html.find_all('div', class_='cancelled'))
            if cancelled:
                continue
            description_doc_url = html.select('a')[0].get('href')
            cells = html.select('td')
            pos_title = cells[1].get_text()
            mil_job_code = cells[2].get_text()
            min_rank, max_rank = cells[3].get_text(
                separator='\n').strip().split('\n')
            print(min_rank, max_rank)

    def get_jobs_data(self, page_BS, processor):
        job_list = page_BS.select(self.JOBTABLECLASS)[0].select('tr')
        if (len(job_list) > 0):
            return (processor(job_list))
        else:
            raise Exception('NY: Error getting job list')

    def crawl(self, website):
        civ_page_bs = self.get_page(website.CIVURL)
        agr_page_bs = self.get_page(website.AGRURL)
        # self.civ_job_list = self.get_jobs_data(civ_page_bs, self.process_civ_data)
        self.agr_list = self.get_jobs_data(agr_page_bs, self.process_agr_data)
        # self.agrDict = self.getAgrJobs(agrPage)


def get_crawler():
    website = NyWebsite()

    return NyCrawler(website)
