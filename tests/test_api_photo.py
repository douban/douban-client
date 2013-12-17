# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main

class TestApiPhoto(DoubanClientTestBase):
    def setUp(self):
        super(TestApiPhoto, self).setUp()
        self.user_id = '40774605'
        self.album_id = '50201880'
        self.photo_id = '1692008281'
        self.comment_id = '113934719'
        self.comment_content = uuid4().hex

    def _add_photo(self):
        with open('douban.png', 'rb') as image:
            return self.client.photo.new(self.album_id, image)

    def test_get_photo(self):
        ret = self.client.photo.get(self.photo_id)

        self.assertEqual(self.photo_id, ret['id'])

    def test_new_photo(self):
        ret = self._add_photo()

        self.assertEqual(self.album_id, ret['album_id'])
        self.assertTrue(ret.has_key('id'))
        self.assertTrue(ret.has_key('desc'))
        self.assertTrue(ret.has_key('alt'))

    def test_delete_photo(self):
        photo = self._add_photo()
        ret = self.client.photo.delete(photo['id'])

        self.assertEqual({}, ret)

    def test_update_photo(self):
        desc = 'hmm'
        ret = self.client.photo.update(self.photo_id, desc)
        self.assertTrue(desc.startswith(ret['desc']))

    def test_like_photo(self):
        ret = self.client.photo.like(self.photo_id)
        self.assertEqual({}, ret)

    def test_unlike_photo(self):
        ret = self.client.photo.unlike(self.photo_id)
        self.assertEqual({}, ret)

    def test_photo_comments(self):
        ret = self.client.photo.comments(self.photo_id)

        self.assertTrue(isinstance(ret['comments'], list))

    def test_get_photo_comment(self):
        ret = self.client.photo.comment.get(self.photo_id, self.comment_id)

        self.assertEqual(self.comment_id, ret['id'])
        self.assertTrue(ret.has_key('content'))

    def test_new_delete_photo_comment(self):
        # new
        ret = self.client.photo.comment.new(self.photo_id, self.comment_content)
        
        self.assertTrue(ret.has_key('id'))
        self.assertTrue(ret.has_key('content'))

        # delete
        comment_id = ret['id']
        ret = self.client.photo.comment.delete(self.photo_id, comment_id)


if __name__ == '__main__':
    main()
