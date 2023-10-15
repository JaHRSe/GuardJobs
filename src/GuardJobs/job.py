class Job:
    def __init__(self,
                 posting_id,
                 branch,
                 pos_title,
                 mil_specialty_code,
                 location,
                 close_date,
                 mil_rank_min,
                 mil_rank_max,
                 canceled,
                 ):
        self.posting_id = posting_id
        self.pos_title = pos_title
        self.mil_rank_min = mil_rank_min,
        self.mil_rank_max = mil_rank_max,
        self.canceled = canceled

    def __str__(self):
        attributes = ', '.join(
            f"{key}={value}" for key, value in self.__dict__.items())
        return f"{self.__class__.__name__}({attributes})"
