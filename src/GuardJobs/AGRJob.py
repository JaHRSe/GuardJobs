from .job import Job


class AGRJob(Job):
    def __init__(self, id, title, adRange, tech_grade, location, close, military_grade):
        super().__init__(id, title)
