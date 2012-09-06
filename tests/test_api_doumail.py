# -*- coding: utf-8 -*-

from uuid import uuid4
from framework import DoubanClientTestBase, DoubanError, main

class TestApiDoumail(DoubanClientTestBase):
    def setUp(self):
        super(TestApiDoumail, self).setUp()
        self.user_id = '51789002'
        self.doumail_id = '263959257'
        self.doumail_ids = ['265897597', '265897596', '265897595']

    def _new_doumail(self):
        title = content = uuid4().hex
        try:
            ret = self.client.doumail.new(title, content, self.user_id)
        except DoubanError, e:
            ret = None
        return ret

    def test_get_doumail(self):
        ret = self.client.doumail.get(self.doumail_id)

        self.assertEqual(self.doumail_id, ret['id'])
        self.assertEqual(self.user_id, ret['receiver']['id'])

    def test_doumail_inbox(self):
        ret = self.client.doumail.inbox()

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(isinstance(ret['mails'], list))

    def test_doumail_outbox(self):
        ret = self.client.doumail.outbox()

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(isinstance(ret['mails'], list))

    def test_doumail_unread(self):
        ret = self.client.doumail.unread()

        self.assertTrue(ret.has_key('start'))
        self.assertTrue(isinstance(ret['mails'], list))

    def test_new_doumail(self):
        ret = self._new_doumail()

        self.assertEqual(None, ret)
    
    def test_read_doumail(self):
        ret = self.client.doumail.read(self.doumail_id)
        print ret
    
    def test_reads_doumail(self):
        ret = self.client.doumail.reads(self.doumail_ids)
        print ret


    def test_delete_doumail(self):
        doumail = self.client.doumail.inbox()
        doumail_id = doumail['mails'][0]['id']
        ret = self.client.doumail.delete(doumail_id)
        
        self.assertEqual({}, ret)

    def test_deletes_doumail(self):
        doumail = self.client.doumail.inbox()
        doumail_ids = [m['id'] for m in doumail['mails']][:2]
        ret = self.client.doumail.deletes(ids=doumail_ids)
   
        self.assertEqual({}, ret)
        

if __name__ == '__main__':
    main()
