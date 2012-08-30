from .base import DoubanApiBase, DEFAULT_START, DEFAULT_COUNT

class People(DoubanApiBase):

    def __repr__(self):
        return '<DoubanAPI People>'

    def get(self, id):
        return self._get('/v2/people/%s'%id)
    
    @property
    def me(self):
        return self.get('~me')

    def search(self, q='', start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/people', q=q, start=start, count=count)
