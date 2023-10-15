from .job import Job


class CivJob(Job):
    def __init__(self, id, pos_title, military_grade, code_title,  ad_range, civ_grade, location, close):
        super().__init__(id=id, pos_title=pos_title, military_grade=military_grade)
        self.ad_range = ad_range
        self.civ_grade = civ_grade
        self.code_title = code_title
        self.location = location
        self.close = close
