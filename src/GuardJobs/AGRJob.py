from .job import Job


class AGRJob(Job):
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
        super().__init__(
            posting_id,
            branch,
            pos_title,
            mil_specialty_code,
            location,
            close_date,
            mil_rank_min,
            mil_rank_max,
            canceled
        )
