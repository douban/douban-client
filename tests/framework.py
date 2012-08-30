# -*- coding: utf-8 -*-

import os
import sys

TEST_DIR = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(TEST_DIR)
sys.path.insert(0, ROOT_DIR)

from unittest import main, TestCase
from douban_client import DoubanClient


KEY = '0af8d9bfca3f0c1a20ea8d3f5ebd244e'
SECRET = 'bf620e8a501e18b6'
CALLBACK = 'http://127.0.0.1:4567/oauth2/callback'
SCOPE = 'douban_basic_common,community_basic_user,community_basic_note'

def get_client():
    client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

    token = 'a7b210cf2f5064d8f716326d8df12e88'

    if token:
        client.auth_by_token(token) 
    else:
        print 'Go to the following link in your browser:' 
        print client.authorize_url

        code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
        client.auth_by_code(code)
        print client.client.token
    return client

client = get_client()

class DoubanClientTestBase(TestCase):
    def setUp(self):
        pass

    @property
    def client(self):
        return client
