#encoding:utf-8

"""
auth with password

注意：auth_with_password 需要先申请 xAuth 权限

关于 xAuth 权限申请可咨询: api-master[at]douban.com
或者到 http://www.douban.com/group/dbapi/ 寻求帮助

"""

from douban_client import DoubanClient

KEY = ''
SECRET = ''
CALLBACK = ''
SCOPE = 'douban_basic_common,community_basic_user'

client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)
client.auth_with_password('user_email', 'user_password')

print client.user.me
