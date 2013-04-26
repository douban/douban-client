# -*- coding: utf-8 -*-


class DoubanBaseError(Exception):
    def __str__(self):
        return "***%s (%s)*** %s" % (self.status, self.reason, self.msg)


class DoubanOAuthError(DoubanBaseError):
    def __init__(self, status, reason, msg={}):
        self.status = status
        self.reason = reason
        self.msg = {}


class DoubanAPIError(DoubanBaseError):

    def __init__(self, resp):
        self.status = resp.status
        self.reason = resp.reason
        self.msg = resp.parsed
