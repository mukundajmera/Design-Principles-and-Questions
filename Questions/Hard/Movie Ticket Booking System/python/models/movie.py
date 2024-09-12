class Movie:
    def __init__(self, movie_id: str, title: str, description: str, duration_in_min: int):
        self._id = movie_id
        self._title = title
        self._description = description
        self._duration_in_min = duration_in_min

    @property
    def duration_in_min(self):
        return self._duration_in_min

