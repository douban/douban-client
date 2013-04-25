# -*- coding: utf-8 -*-

from pyoauth2 import AccessToken

from .error import DoubanAPIError, DoubanOAuthError

DEFAULT_START = 0
DEFAULT_COUNT = 20


def check_execption(func):
    def _check(*arg, **kws):
        resp = func(*arg, **kws)
        if resp.status >= 400:
            raise DoubanAPIError(resp)
        return resp.parsed
    return _check


class DoubanApiBase(object):

    def __init__(self, access_token):
        self.access_token = access_token
        if not isinstance(self.access_token, AccessToken):
            raise DoubanOAuthError(401, 'UNAUTHORIZED')

    def __repr__(self):
        return '<DoubanAPI Base>'

    @check_execption
    def _get(self, url, **opts):
        return self.access_token.get(url, **opts)

    @check_execption
    def _post(self, url, **opts):
        return self.access_token.post(url, **opts)

    @check_execption
    def _put(self, url, **opts):
        return self.access_token.put(url, **opts)

    @check_execption
    def _patch(self, url, **opts):
        return self.access_token.patch(url, **opts)

    @check_execption
    def _delete(self, url, **opts):
        return self.access_token.delete(url, **opts)
