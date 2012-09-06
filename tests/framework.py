# -*- coding: utf-8 -*-

import os
import sys

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)

from unittest import main, TestCase
from douban_client import DoubanClient
from douban_client.api.error import DoubanError


KEY = ''
SECRET = ''
CALLBACK = ''

SCOPE_MAP = {
             'basic': ['douban_basic_common', 'community_basic_user'],
             'note': ['community_basic_note'],
             'miniblog': ['shuo_basic_r', 'shuo_basic_w', 'shuo_private'],
             'doumail': ['community_advanced_doumail_r', 'community_advanced_doumail_w'],
             'online': ['community_basic_online', 'community_advanced_online'],
             'photo': ['community_basic_photo', 'community_advanced_photo'],
             'music': ['music_basic_r', 'music_basic_w'],
             'movie': ['movie_basic_r', 'movie_basic_w'],
             'book': ['book_basic_r', 'book_basic_w'],
             'event': ['event_basic_r', 'event_basic_w'],
            }

SCOPE = ','.join(reduce(lambda x, y: x + y, SCOPE_MAP.values()))

def get_client():
    client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

    token = ''

    if token:
        client.auth_with_token(token) 
    else:
        print 'Go to the following link in your browser:' 
        print client.authorize_url

        code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
        client.auth_with_code(code)
        print client.client.token
    return client

client = get_client()

class DoubanClientTestBase(TestCase):
    def setUp(self):
        pass

    @property
    def client(self):
        return client
