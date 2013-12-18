# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, main


class TestApiNote(DoubanClientTestBase):
    def setUp(self):
        super(TestApiNote, self).setUp()
        self.user_id = '64129916'
        self.note_id = '321263424'
        self.comment_id = '36366425'
        self.comment_content = uuid4().hex
        self.title = 'test note title'
        self.content = 'test note content'
        self.update_content = 'test note was updated'

    def _new_note(self):
        return self.client.note.new(self.title, self.content)

    def test_get_note_list(self):
        ret = self.client.note.list(self.user_id)

        self.assertTrue('start' in ret)
        self.assertTrue('count' in ret)
        self.assertTrue('notes' in ret)
        self.assertTrue(isinstance(ret['notes'], list))

    def test_get_note(self):
        ret = self.client.note.get(self.note_id)

        self.assertEqual(ret['id'], self.note_id)
        self.assertTrue('title' in ret)
        self.assertTrue('summary' in ret)
        self.assertTrue('content' in ret)

    def test_new_note(self):
        ret = self._new_note()
        self.assertEqual(ret['title'], self.title)
        self.assertTrue('content' in ret)

    def test_update_note(self):
        ret = self._new_note()
        self.assertTrue('id' in ret)
        note_id = ret.get('id')
        self.assertTrue(note_id)
        ret = self.client.note.update(note_id, self.title, self.update_content)

        # TODO
        # 这个地方很奇怪，更新成功，但是应该返回结果类型是 unicode，说好的 JSON 呢
        # self.assertEqual(ret['title'], self.title)
        # self.assertEqual(ret['content'], self.update_content)

        self.assertTrue(self.update_content in ret)

    def test_upload_note_photo(self):
        note = self._new_note()
        self.assertTrue('id' in note)
        note_id = note.get('id')
        self.assertTrue(note_id)

        pid = 1
        content = self.update_content
        layout = 'L'
        desc = 'desc for image%s' % pid
        with open('douban.png', 'rb') as image:
            ret = self.client.note.upload_photo(note_id, pid, image, content, layout, desc)
            self.assertTrue('content' in ret)

    def test_delete_note(self):
        note = self._new_note()
        ret = self.client.note.delete(note['id'])
        self.assertEqual(ret, {})

    def test_get_liked(self):
        ret = self.client.note.liked_list(self.user_id)
        self.assertTrue('start' in ret)
        self.assertTrue('count' in ret)
        self.assertTrue('notes' in ret)
        self.assertTrue(isinstance(ret['notes'], list))

    def test_like(self):
        ret = self.client.note.like(self.note_id)
        self.assertEqual(ret, {})

    def test_unlike(self):
        ret = self.client.note.unlike(self.note_id)
        self.assertEqual(ret, {})

    def test_note_comments(self):
        ret = self.client.note.comments(self.note_id)
        self.assertTrue(isinstance(ret['comments'], list))

    def test_get_note_comment(self):
        ret = self.client.note.comment.get(self.note_id, self.comment_id)
        self.assertEqual(self.comment_id, ret['id'])
        self.assertTrue('content' in ret)

    def test_new_delete_note_comment(self):
        # new
        ret = self.client.note.comment.new(self.note_id, self.comment_content)
        self.assertTrue('id' in ret)
        self.assertTrue('content' in ret)
        # delete
        comment_id = ret['id']
        ret = self.client.note.comment.delete(self.note_id, comment_id)
        self.assertEqual({}, ret)


if __name__ == '__main__':
    main()
