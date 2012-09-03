# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiMusic(DoubanClientTestBase):
    def setUp(self):
        super(TestApiMusic, self).setUp()
        self.user_id = '40774605'
        self.music_id = '11524982'
        self.title = "this is a good album"
        self.content = "wanting wanting wanting"

    """
    def test_get_music(self):
        ret = self.client.music.get(self.music_id)
        self.assertEqual(ret['id'], self.music_id)
    """

if __name__ == '__main__':
    main()
