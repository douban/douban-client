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


if __name__ == '__main__':
    main()
