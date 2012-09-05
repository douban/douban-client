# -*- coding: utf-8 -*-

from uuid import uuid4
from datetime import datetime
from framework import DoubanClientTestBase, main

class TestApiEvent(DoubanClientTestBase):
    
    def setUp(self):
        self.event_id = '17080169'
        self.user_id = '40774605'
        self.loc = '108288'
        self.participate_date = datetime.now().strftime('%Y-%m-%d')

    def test_get_event(self):
        ret = self.client.event.get(self.event_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertEqual(self.event_id, ret['id'])
        self.assertTrue(ret.has_key('location'))

    def test_get_event_participants(self):
        ret = self.client.event.participants(self.event_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['users'], list))
        self.assertTrue(ret.has_key('total'))

    def test_get_event_wishers(self):
        ret = self.client.event.wishers(self.event_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['users'], list))
        self.assertTrue(ret.has_key('total'))

    def test_get_user_owned_events(self):
        ret = self.client.event.owned(self.user_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['events'], list))

    def test_get_user_participated_events(self):
        ret = self.client.event.participated(self.user_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['events'], list))

    def test_get_user_wished_events(self):
        ret = self.client.event.wished(self.user_id)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['events'], list))

    def test_event_list(self):
        ret = self.client.event.list(self.loc)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['events'], list))

    def test_search_event(self):
        ret = self.client.event.search('北京', self.loc)

        self.assertTrue(isinstance(ret, dict))
        self.assertTrue(isinstance(ret['events'], list))

    # def test_join_event(self):
    #     ret = self.client.event.join(self.event_id, '2012-')
    #     print ret


    def test_quit_event(self):
        ret = self.client.event.quit(self.event_id)
        
        self.assertEqual({}, ret)

    def test_wish_event(self):
        ret = self.client.event.wish(self.event_id)

        self.assertEqual({}, ret)

    def test_unwish_event(self):
        ret = self.client.event.unwish(self.event_id)

        self.assertEqual({}, ret)


if __name__ == '__main__':
    main()
