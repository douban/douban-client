# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiPeople(DoubanClientTestBase):

    def setUp(self):
        super(TestApiPeople, self).setUp()
        self.user_id = '40774605'

    def test_get_people(self):
        ret = self.client.people.get('liluoliluo')
        self.assertEqual(ret['uid'], 'liluoliluo')

    def test_get_me(self):
        ret = self.client.people.me
        self.assertTrue(ret.has_key('id'))

    def test_search(self):
        q = '落'
        ret = self.client.people.search(q)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('total'))

    def test_follow(self):
        ret = self.client.people.follow(self.user_id)
        
        self.assertTrue(ret['following'])

    def test_unfollow(self):
        self.client.people.follow(self.user_id)
        ret = self.client.people.unfollow(self.user_id)

        self.assertFalse(ret['following'])

    def test_block(self):
        ret = self.client.people.block(self.user_id)

        self.assertTrue(ret)

    def test_friendships(self):
        ret = self.client.people.friendships(target_id='51789002')

        self.assertEqual(set(['source', 'target']), set(ret.keys()))
        self.assertTrue(ret['source'].has_key('following'))
        self.assertTrue(ret['target'].has_key('following'))

    def test_following(self):
        ret = self.client.people.following(self.user_id)

        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all([r.has_key('uid') for r in ret]))

    def test_followers(self):
        ret = self.client.people.followers(self.user_id)

        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all([r.has_key('uid') for r in ret]))

    def test_follow_in_common(self):
        ret = self.client.people.follow_in_common(self.user_id)

        self.assertTrue(isinstance(ret, list))
        self.assertTrue(all([r.has_key('uid') for r in ret]))


    def test_following_followers_of(self):
        ret = self.client.people.following_followers_of('51789002')
        print ret


    # def test_suggestions(self):
    #     ret = self.client.people.suggestions(self.user_id)

    #     self.assertTrue(isinstance(ret, list))
    #     self.assertTrue(all([r.has_key('uid') for r in ret]))
        


if __name__ == '__main__':
    main()
