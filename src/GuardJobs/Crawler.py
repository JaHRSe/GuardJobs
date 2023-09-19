from bs4 import BeautifulSoup
from urllib.request import urlopen


class Crawler:
    def __init__(self, website):
        self.website = website
        self.html = self.getPage(website.url)

    def getPage(self, url):
        try:
            html = urlopen(url)
        except Exception as e:
            print(e)
            return None
        return BeautifulSoup(html, 'html.parser')

    def safeGet(bs, selector):
        selectedElems = bs.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''

    def crawl(self):
        pass
