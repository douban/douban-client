# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiGuess(DoubanClientTestBase):
    def setUp(self):
        super(TestApiGuess, self).setUp()
        self.user_id = '40774605'

    def test_guess_notes(self):
        ret = self.client.guess.notes(self.user_id)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('notes'))
        self.assertTrue(isinstance(ret['notes'], list))

    def test_guess_albums(self):
        ret = self.client.guess.albums(self.user_id)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('albums'))
        self.assertTrue(isinstance(ret['albums'], list))


if __name__ == '__main__':
    main()
