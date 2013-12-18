# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main

class TestApiAlbum(DoubanClientTestBase):
    def setUp(self):
        super(TestApiAlbum, self).setUp()
        self.user_id = '40774605'
        self.album_id = '50201880'

    def test_get_album(self):
        ret = self.client.album.get(self.album_id)
        
        self.assertEqual(self.album_id, ret['id'])
        self.assertTrue('liked' in ret)

    def test_new_album(self):
        ret = self.client.album.new('test', desc='ddddddddddddd')
        
        self.assertTrue('id' in ret)
        self.assertTrue('privacy' in ret)
        self.assertTrue('size' in ret)
        self.assertTrue('author' in ret)

    def test_update_album(self):
        new_title = uuid4().hex
        self.client.album.update(self.album_id, new_title, 'new_desc')
        ret = self.client.album.get(self.album_id)
        self.assertEqual(new_title, ret['title'])

    def test_delete_album(self):
        aid = self.client.album.new('test', desc='abcdefg')['id']
        ret = self.client.album.delete(aid)

        self.assertEqual({}, ret)

    def test_album_list_by_user(self):
        ret = self.client.album.list(self.user_id)
        
        self.assertTrue(isinstance(ret, dict))
        self.assertTrue('albums' in ret)
        self.assertTrue(isinstance(ret['albums'], list))

    def test_liked_album(self):
        ret = self.client.album.liked_list(self.user_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue('albums' in ret)
        self.assertTrue(isinstance(ret['albums'], list))

    def test_get_photos(self):
        ret = self.client.album.photos(self.album_id)

        self.assertTrue('start' in ret)
        self.assertTrue('count' in ret)
        self.assertTrue('photos' in ret)
        self.assertTrue(isinstance(ret['photos'], list))

    def test_like_album(self):
        ret = self.client.album.like(self.album_id)

        self.assertEqual({}, ret)

    def test_unlike_album(self):
        ret = self.client.album.unlike(self.album_id)

        self.assertEqual({}, ret)


if __name__ == '__main__':
    main()
