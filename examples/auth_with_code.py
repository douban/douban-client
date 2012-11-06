from douban_client import DoubanClient

KEY = ''
SECRET = ''
CALLBACK = ''

SCOPE = 'douban_basic_common,community_basic_user'
client = DoubanClient(KEY, SECRET, CALLBACK, SCOPE)

print client.authorize_url
code = raw_input('Enter the verification code:') 

client.auth_with_code(code) 
print client.user.me
