from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class Guess(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI Guess>'

    def notes(self, user_id):
        return self._get('/v2/note/people_notes/%s/guesses'%user_id)
