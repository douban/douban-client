# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiUser(DoubanClientTestBase):

    def setUp(self):
        super(TestApiUser, self).setUp()
        self.user_id = '70920446'

    def test_get_user(self):
        ret = self.client.user.get('liluoliluo')
        self.assertEqual(ret['uid'], 'liluoliluo')

    def test_get_me(self):
        ret = self.client.user.me
        self.assertTrue(ret.has_key('id'))

    def test_search(self):
        q = '落'
        ret = self.client.user.search(q)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('total'))

    def test_follow(self):
        ret = self.client.user.follow(self.user_id)

        self.assertTrue(ret['following'])

    def test_unfollow(self):
        self.client.user.follow(self.user_id)
        ret = self.client.user.unfollow(self.user_id)

        self.assertFalse(ret['following'])

    def test_following(self):
        ret = self.client.user.following(self.user_id)

        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all([r.has_key('uid') for r in ret]))

    def test_followers(self):
        ret = self.client.user.followers(self.user_id)

        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all([r.has_key('uid') for r in ret]))

    # def test_following_followers_of(self):
    #     ret = self.client.user.following_followers_of('51789002')


    # def test_suggestions(self):
    #     ret = self.client.user.suggestions(self.user_id)

    #     self.assertTrue(isinstance(ret, list))
    #     self.assertTrue(all([r.has_key('uid') for r in ret]))



if __name__ == '__main__':
    main()
