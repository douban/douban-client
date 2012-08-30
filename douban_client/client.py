# -*- coding: utf-8 -*-

from oauth2 import Client, AccessToken
from api import DoubanApi

class DoubanClient(DoubanApi):

    API_HOST = 'https://api.douban.com'
    AUTH_HOST = 'https://www.douban.com'
    TOKEN_URL = AUTH_HOST + '/service/auth2/token'
    AUTHORIZE_URL = AUTH_HOST + '/service/auth2/auth'
    

    def __init__(self, key, secret, redirect='', scope=''):
        self.redirect_uri = redirect
        self.scope = scope
        self.client = Client(key, secret, 
                       site=self.API_HOST, authorize_url=self.AUTHORIZE_URL, token_url=self.TOKEN_URL)

    def __repr__(self):
        return '<DoubanClient OAuth2>'

    @property
    def authorize_url(self):
        return self.client.auth_code.authorize_url(redirect_uri=self.redirect_uri, scope=self.scope)

    def auth_by_code(self, code):
        self.client = self.client.auth_code.get_token(code, redirect_uri=self.redirect_uri)

    def auth_by_token(self, token):
        self.client = AccessToken(self.client, token)
