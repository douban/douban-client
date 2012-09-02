# -*- coding: utf-8 -*-

from .error import DoubanError

DEFAULT_START = 0
DEFAULT_COUNT = 20

def check_execption(func):
    def _check(*arg, **kws):
        resp = func(*arg, **kws)
        if resp.status >= 400:
            raise DoubanError(resp)
        return resp.parsed
    return _check


class DoubanApiBase(object):

    def __init__(self, client):
        self.client = client

    def __repr__(self):
        return '<DoubanAPI Base>'
    
    @check_execption
    def _get(self, url, **opts):
        return self.client.get(url, **opts)

    @check_execption
    def _post(self, url, **opts):
        return self.client.post(url, **opts)

    @check_execption
    def _put(self, url, **opts):
        return self.client.put(url, **opts)

    @check_execption
    def _patch(self, url, **opts):
        return self.client.patch(url, **opts)

    @check_execption
    def _delete(self, url, **opts):
        return self.client.delete(url, **opts)
