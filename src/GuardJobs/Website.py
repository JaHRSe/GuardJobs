from abc import ABC, abstractclassmethod
from bs4 import BeautifulSoup


class Website(ABC):
    def __init__(self, name, url, techUrl, agrUrl):
        self.name = name
        self.homePage = url
        self.techUrl = techUrl
        self.agrUrl = agrUrl
