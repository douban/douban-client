# -*- coding: utf-8 -*-

from pyoauth2 import Client, AccessToken
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
        self.access_token = None

    def __repr__(self):
        return '<DoubanClient OAuth2>'

    @property
    def authorize_url(self):
        return self.client.auth_code.authorize_url(redirect_uri=self.redirect_uri, scope=self.scope)

    def auth_with_code(self, code):
        self.access_token = self.client.auth_code.get_token(code, redirect_uri=self.redirect_uri)

    def auth_with_token(self, token):
        self.access_token = AccessToken(self.client, token)

    def auth_with_password(self, username, password, **opt):
        self.access_token = self.client.password.get_token(username=username,
                                 password=password, redirect_uri=self.redirect_uri, **opt)

    @property
    def token_code(self):
        return self.access_token and self.access_token.token

    @property
    def refresh_token_code(self):
        return getattr(self.access_token, 'refresh_token', None)

    def refresh_token(self, refresh_token):
        access_token = AccessToken(self.client, token='', refresh_token=refresh_token)
        self.access_token = access_token.refresh()
