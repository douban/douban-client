from douban_client import DoubanClient

KEY = ''
SECRET = ''
CALLBACK = ''
TOKEN = 'your token'

SCOPE = 'douban_basic_common,community_basic_user'
client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

cleint.auth_with_token(TOKEN)
print client.user.me
