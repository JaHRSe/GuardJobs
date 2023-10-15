from bs4 import BeautifulSoup
from urllib.request import urlopen
from abc import ABC, abstractclassmethod


class Crawler(ABC):
    # def __init__(self, website):
    # self.website = website

    def get_page(self, url):
        try:
            html = urlopen(url)
        except Exception as e:
            print(e)
            return None
        return BeautifulSoup(html, 'html.parser')

    def safe_get(self, bs, selector):
        """return text form html object
            ARGS:
                bs (BeutifulSoup): Object with target HTML
                selector (string): Selector used to extract text
            Returns:
                string: Text from HTML target element or empty string if not found
        """
        selectedElems = bs.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return [elem.get_text() for elem in selectedElems]
        return None

    @abstractclassmethod
    def get_jobs_data(self):
        """returns array of  job objects, generic for each job type"""
        pass

    @abstractclassmethod
    def crawl(self):
        """Crawls link(s) to gather raw html of all jobs"""
        pass
