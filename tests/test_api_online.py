# -*- coding: utf-8 -*-

from uuid import uuid4
from datetime import datetime, timedelta
from framework import DoubanClientTestBase, main

t2s = lambda t: t.strftime('%Y-%m-%d %H:%M')
now = datetime.now()
begin_time = t2s(now)
end_time  = t2s(now + timedelta(days=1))

class TestApiOnline(DoubanClientTestBase):
    def setUp(self):
        super(TestApiOnline, self).setUp()
        self.user_id = '40774605'
        self.online_id = '11182611'
        self._title = 'api douban-client test'
        self._desc = 'api test, desc abcdefg hijklmn opq rst uvw xyz, now you see, i can create online.'
        self.discussion_title = uuid4().hex
        self.discussion_content = uuid4().hex
    

    def _add_online(self):
        return self.client.online.new(self._title, self._desc, begin_time, end_time)


    def test_get_online(self):
        ret = self.client.online.get(self.online_id)

        self.assertEqual(self.online_id, ret['id'])
        self.assertEqual('http://www.douban.com/online/%s/'%self.online_id, ret['alt'])

    def test_new_online(self):
        ret = self._add_online()

        self.assertEqual(self._title, ret['title'])
        self.assertEqual(self._desc, ret['desc'])

    def test_update_online(self):
        online = self._add_online()
        new_title = self._title + 'new'
        new_desc = self._desc + 'new'
        ret = self.client.online.update(online['id'], new_title, new_desc, begin_time, end_time)

        self.assertEqual(new_title, ret['title'])
        self.assertEqual(new_desc, ret['desc'])

    def test_delete_online(self):
        online = self._add_online()
        ret = self.client.online.delete(online['id'])
        
        self.assertEqual({}, ret)

    def test_join_online(self):
        ret = self.client.online.join(self.online_id)

        self.assertEqual({}, ret)

    def test_quit_online(self):
        ret = self.client.online.quit(self.online_id)

        self.assertEqual({}, ret)

    def test_like_online(self):
        ret = self.client.online.like(self.online_id)

        self.assertEqual({}, ret)

    def test_unlike_online(self):
        ret = self.client.online.unlike(self.online_id)

        self.assertEqual({}, ret)

    def test_get_online_participants(self):
        ret = self.client.online.participants(self.online_id)

        self.assertTrue(ret.has_key('total'))
        self.assertTrue(isinstance(ret['users'], list))

    def test_get_online_discussions(self):
        ret = self.client.online.discussions(self.online_id)

        self.assertTrue(isinstance(ret['discussions'], list))

    def test_online_list(self):
        ret = self.client.online.list(cate='day')

        self.assertTrue(ret.has_key('total'))
        self.assertTrue(isinstance(ret['onlines'], list))

    def test_new_online_discussion(self):
        ret = self.client.online.discussion.new(self.online_id, 
                self.discussion_title, self.discussion_content)

        self.assertTrue(self.discussion_title, ret['title'])
        self.assertTrue(self.discussion_content, ret['content'])

    def test_owned_onlines(self):
        ret = self.client.online.owned(self.user_id)

        self.assertTrue(ret.has_key('total'))
        self.assertTrue(isinstance(ret['onlines'], list))

    def test_joined_onlines(self):
        ret = self.client.online.joined(self.user_id)

        self.assertTrue(ret.has_key('total'))
        self.assertTrue(isinstance(ret['onlines'], list))



if __name__ == '__main__':
    main()
