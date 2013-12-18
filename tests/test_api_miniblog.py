# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, DoubanAPIError, main


class TestApiMiniblog(DoubanClientTestBase):

    def setUp(self):
        super(TestApiMiniblog, self).setUp()
        self.user_id = '40774605'
        self.miniblog_id = '999242853'
        self.comment = uuid4().hex
        self.comment_id = '140907103'
        self.rec_title = 'rec from douban-client'
        self.rec_url = 'https://github.com/douban/douban-client'
        self.rec_desc = 'Python client library for Douban APIs (OAuth 2.0) '
        self.rec_image = 'http://img3.douban.com/view/photo/photo/public/p1850826843.jpg'

    def _gen_text(self):
        return 'test miniblog %s by douban-client'% uuid4().hex

    def _new_miniblog(self, upload=False):
        image = upload and open('douban.png', 'rb')
        ret = self.client.miniblog.new(self._gen_text(), image=image)
        if image:
            image.close()
        return ret

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

    def test_new_miniblog(self):
        ret = self._new_miniblog()
        self.assertTrue(isinstance(ret, dict))
        self.assertTrue('id' in ret)

    def test_new_miniblog_with_image(self):
        ret = self._new_miniblog(upload=True)
        self.assertTrue('id' in ret)

    def test_delete_miniblog(self):
        mb = self._new_miniblog()
        mid = mb['id']
        self.client.miniblog.delete(mid)
        func = self.client.miniblog.get
        self.assertRaises(DoubanAPIError, func, mid)

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

    def test_get_miniblog_comments(self):
        ret = self.client.miniblog.comments(self.miniblog_id)
        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all(['user' in r for r in ret]))

    def test_new_delete_miniblog_comment(self):
        # new
        ret = self.client.miniblog.comment.new(self.miniblog_id, self.comment)
        self.assertEqual(self.comment, ret['text'])
        # delete
        comment_id = ret['id']
        ret = self.client.miniblog.comment.delete(comment_id)
        self.assertEqual(self.comment, ret['text'])

    def test_get_miniblog_comment(self):
        ret = self.client.miniblog.comment.get(self.comment_id)
        self.assertEqual('456', ret['text'])

    def test_miniblog_rec(self):
        ret = self.client.miniblog.rec(title=self.rec_title, url=self.rec_url,
                desc=self.rec_desc, image=self.rec_image)
        self.assertTrue('title' in ret)
        self.assertEqual(len(ret['attachments']), 1)


if __name__ == '__main__':
    main()
