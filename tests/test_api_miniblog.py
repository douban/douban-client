# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, DoubanError, main

class TestApiMiniblog(DoubanClientTestBase):

    def setUp(self):
        super(TestApiMiniblog, self).setUp()
        self.user_id = '40774605'
        self.miniblog_id = '999242853'

    def _gen_text(self):
        return 'test miniblog %s by douban-client'% uuid4().hex

    def _new_miniblog(self, upload=False):
        image = upload and open('douban.png')
        return self.client.miniblog.new(self._gen_text(), image=image)

    def test_get_miniblog(self):
        ret = self.client.miniblog.get(self.miniblog_id)

        self.assertTrue(isinstance(ret, dict))

    def test_home_timeline(self):
        ret = self.client.miniblog.home_timeline()

        self.assertTrue(isinstance(ret, list))

    def test_user_timeline(self):
        ret = self.client.miniblog.user_timeline(self.user_id)
        
        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all([self.user_id == r['user']['id'] for r in ret]))

    def test_mentions(self):
        uid = self.client.people.me['uid']
        ret = self.client.miniblog.mentions()

        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all([isinstance(r, dict) for r in ret]))
        self.assertTrue(all([r.has_key('id') for r in ret]))
        self.assertTrue(all([r.has_key('unread') for r in ret]))

    def test_new_miniblog(self):
        ret = self._new_miniblog()
        
        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(ret.has_key('id'))

    def test_new_miniblog_with_image(self):
        ret = self._new_miniblog(upload=True)

        self.assertTrue(ret.has_key('id'))
        self.assertEqual('upload', ret['type'])


    def test_delete_miniblog(self):
        mb = self._new_miniblog()
        mid = mb['id']
        self.client.miniblog.delete(mid)
        func = self.client.miniblog.get

        self.assertRaises(DoubanError, func, mid)

    def test_like_unlike_likers_miniblog(self):
        mb = self._new_miniblog()
        mid = mb['id']

        ret = self.client.miniblog.like(mid)
        self.assertTrue(ret['liked'])

        ret = self.client.miniblog.unlike(mid)
        self.assertFalse(ret['liked'])

        ret = self.client.miniblog.likers(mid)
        self.assertTrue(isinstance(ret, list))

    def test_reshare_unreshare_resharers_miniblog(self):
        mid = self.miniblog_id

        # reshare
        self.client.miniblog.reshare(mid)
        ret = self.client.miniblog.get(mid)
        reshared_count = ret['reshared_count']
   
        self.assertTrue(reshared_count > 0)

        # unreshare
        # 这个豆瓣广播还没有实现接口
        # self.client.miniblog.unreshare(mid)
        # ret = self.client.miniblog.get(mid)
        #
        #self.assertEqual(reshared_count-1, ret['reshared_count'])

        # reshareders
        ret = self.client.miniblog.reshareders(mid)
        self.assertTrue(isinstance(ret, list))

if __name__ == '__main__':
    main()
