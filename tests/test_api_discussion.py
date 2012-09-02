# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main

class TestApiDiscussion(DoubanClientTestBase):
    def setUp(self):
        super(TestApiDiscussion, self).setUp()
        self.user_id = '40774605'
        self.discussion_id = '48549097'
        self.target = 'online'
        self.target_id = '10903196'
        
        tmp = uuid4().hex

        self.title = tmp
        self.content = tmp

    def _add_discussion(self):
        return self.client.discussion.new(self.target, self.target_id, self.title, self.content)


    def test_get_discussion(self):
        ret = self.client.discussion.get(self.discussion_id)

        self.assertEqual(self.discussion_id, ret['id'])
        self.assertTrue(ret.has_key('author'))
        self.assertTrue(ret.has_key('content'))

    def test_update_discussion(self):
        content = title = uuid4().hex
        ret = self.client.discussion.update(self.discussion_id, title, content)

        self.assertTrue(title, ret['title'])
        self.assertTrue(content, ret['content'])

    def test_new_discussion(self):
        ret = self._add_discussion()

        self.assertTrue(self.title, ret['title'])
        self.assertTrue(self.content, ret['content'])
        self.assertTrue(self.target in ret['alt'])
        self.assertTrue(self.target_id in ret['alt'])

    def test_delete_discussion(self):
        dis = self._add_discussion()
        ret = self.client.discussion.delete(dis['id'])

        self.assertEqual({}, ret)

    def test_discussion_list(self):
        ret = self.client.discussion.list(self.target, self.target_id)

        self.assertTrue(isinstance(ret['discussions'], list))

if __name__ == '__main__':
    main()
