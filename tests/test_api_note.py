# -*- coding: utf-8 -*-

from framework import DoubanClientTestBase, main

class TestApiNote(DoubanClientTestBase):
    def setUp(self):
        super(TestApiNote, self).setUp()
        self.user_id = '40774605'
        self.note_id = '234002802'
        self.title = 'test note title'
        self.content = 'test note content'
        self.update_content = 'test note was updated'

    def _new_note(self):
        return self.client.note.new(self.title, self.content)

    def test_get_note_list(self):
        ret = self.client.note.list(self.user_id)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('notes'))
        self.assertTrue(isinstance(ret['notes'], list))

    def test_get_note(self):
        ret = self.client.note.get(self.note_id)

        self.assertEqual(ret['id'], self.note_id)
        self.assertTrue(ret.has_key('title'))
        self.assertTrue(ret.has_key('summary'))
        self.assertTrue(ret.has_key('content'))

    def test_new_note(self):
        ret = self._new_note()
        self.assertEqual(ret['title'], self.title)
        self.assertTrue(ret.has_key('content'))
        

    def test_update_note(self):
        ret = self.client.note
        # TODO
        # ret = self.client.note.update(self.note_id, self.title, self.update_content)

        # self.assertEqual(ret['title'], self.title)
        # self.assertEqual(ret['content'], self.update_content)

    def test_delete_note(self):
        note = self._new_note()
        ret = self.client.note.delete(note['id'])

        self.assertEqual(ret, {})

    def test_get_liked(self):
        ret = self.client.note.liked_list(self.user_id)

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(ret.has_key('count'))
        self.assertTrue(ret.has_key('notes'))
        self.assertTrue(isinstance(ret['notes'], list))

    def test_like(self):
        ret = self.client.note.like(self.note_id)
        self.assertEqual(ret, {})

    def test_unlike(self):
        ret = self.client.note.unlike(self.note_id)
        self.assertEqual(ret, {})


if __name__ == '__main__':
    main()
