# -*- coding: utf-8 -*-

from .base import DoubanAPIBase, DEFAULT_START, DEFAULT_COUNT
from .comment import Comment

class Note(DoubanAPIBase):

    target = 'note'

    def __repr__(self):
        return '<DoubanAPI Note>'

    def new(self, title, content, privacy='public', can_reply='true'):
        return self._post('/v2/notes',
                title=title, content=content, privacy=privacy, can_reply=can_reply)


    def get(self, id, format='text'):
        return self._get('/v2/note/%s'%id, format=format)

    def update(self, id, title, content, privacy='public', can_reply='true'):
        return self._put('/v2/note/%s'%id,
                title=title, content=content, privacy=privacy, can_reply=can_reply)

    def upload_photo(self, id, pid, image, content, layout=None, desc=None):
        kwargs = {
            'pids': 'p_%s' % pid,
            'content': content,
            'layout_%s' % pid: layout,
            'desc_%s' % pid: desc
        }
        files = {
            'image_%s' % pid: image
        }
        return self._post('/v2/note/%s' % id, files=files, **kwargs)

    def delete(self, id):
        return self._delete('/v2/note/%s'%id)

    def like(self, id):
        return self._post('/v2/note/%s/like'%id)

    def unlike(self, id):
        return self._delete('/v2/note/%s/like'%id)

    def list(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/note/user_created/%s'%user_id, start=start, count=count)

    def liked_list(self, user_id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return self._get('/v2/note/user_liked/%s'%user_id, start=start, count=count)

    def comments(self, id, start=DEFAULT_START, count=DEFAULT_COUNT):
        return Comment(self.access_token, self.target).list(id, start=start, count=count)

    @property
    def comment(self):
        return Comment(self.access_token, self.target)
