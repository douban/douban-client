# -*- coding: utf-8 -*-

DEFAULT_START = 0
DEFAULT_COUNT = 20

class DoubanApiBase(object):

    def __init__(self, client):
        self.client = client

    def __repr__(self):
        return '<DoubanAPI Base>'

    def _get(self, url, **opts):
        return self.client.get(url, **opts).parsed

    def _post(self, url, **opts):
        return self.client.post(url, **opts).parsed

    def _put(self, url, **opts):
        return self.client.put(url, **opts).parsed

    def _patch(self, url, **opts):
        return self.client.patch(url, **opts).parsed

    def _delete(self, url, **opts):
        return self.client.delete(url, **opts).parsed
