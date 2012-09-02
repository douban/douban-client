# -*- coding: utf-8 -*-

class DoubanError(Exception):
    
    def __init__(self, resp):
        self.status = resp.status
        self.reason = resp.reason
        self.msg = resp.parsed

    def __str__(self):
        return "***%s (%s)*** %s"%(self.status, self.reason, self.msg)
