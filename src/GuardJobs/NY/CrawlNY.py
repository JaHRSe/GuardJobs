from src.GuardJobs.Website import Website
from src.GuardJobs.Crawler import Crawler

website = Website('DMNA', "https://dmna.ny.gov/jobs/", "jobnavtable")


class NyCrawler(Crawler):
    pass


def getCrawler():
    return NyCrawler(website)
