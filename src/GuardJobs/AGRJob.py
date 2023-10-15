from .job import Job


class AGRJob(Job):
    def __init__(self, id, pos_title, ad_range, location, close, military_grade):
        super().__init__(id, pos_title, military_grade)
        self.ad_range = ad_range
        self.location = location
        self.close = close
