# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiPeople(DoubanClientTestBase):

    def test_get_people(self):
        ret = self.client.people.get('liluoliluo')
        self.assertEqual(ret['uid'], 'liluoliluo')

    def test_get_me(self):
        ret = self.client.people.me
        self.assertTrue(ret.has_key('id'))

    def test_search(self):
        kw = '落'
        ret = self.client.people.search(q=kw)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('total'))


if __name__ == '__main__':
    main()
