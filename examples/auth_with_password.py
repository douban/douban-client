from douban_client import DoubanClient

KEY = ''
SECRET = ''
CALLBACK = ''

SCOPE = 'douban_basic_common,community_basic_user'
client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

client.auth_with_password('user_email', 'user_password') 
print client.user.me
