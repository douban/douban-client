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
        self.assertTrue(ret.has_key('liked'))

    # def test_new_album(self):
    #     ret = self.client.album.new('test', desc='ddddddddddddd')
    #     
    #     self.assertTrue(ret.has_key('id'))
    #     self.assertTrue(ret.has_key('privacy'))
    #     self.assertTrue(ret.has_key('size'))
    #     self.assertTrue(ret.has_key('author'))

    # def test_update_album(self):
    #     new_title = uuid4().hex
    #     ret = self.client.album.update(self.album_id, new_title)
    #     self.assertEqual(new_title, ret['title'])

    def test_delete_album(self):
        aid = self.client.album.new('test', desc='abcdefg')['id']
        ret = self.client.album.delete(aid)

        self.assertEqual({}, ret)

    def test_album_list_by_user(self):
        ret = self.client.album.list(self.user_id)
        
        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(ret.has_key('albums'))
        self.assertTrue(isinstance(ret['albums'], list))

    def test_liked_album(self):
        ret = self.client.album.liked_list(self.user_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(ret.has_key('albums'))
        self.assertTrue(isinstance(ret['albums'], list))

    def test_get_photos(self):
        ret = self.client.album.photos(self.album_id)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('photos'))
        self.assertTrue(isinstance(ret['photos'], list))

    # def test_like_album(self):
    #     ret = self.client.album.like(self.album_id)

    # def test_unlike_album(self):
    #     ret = self.client.album.unlike(self.album_id)


if __name__ == '__main__':
    main()
