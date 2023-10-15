class Job:
    def __init__(self, id, pos_title, military_grade):
        self.id = id
        self.pos_title = pos_title
        self.military_grade = military_grade

    def __str__(self):
        attributes = ', '.join(
            f"{key}={value}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"
