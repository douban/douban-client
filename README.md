## douban-client

douban-client 是对豆瓣 API v2 接口进行了一个简单封装，主要包括了 OAuth 2.0 认证、图片上传以及接口方面的调用。

目前已完成的接口有：
``` 
* 用户 People
* 广播 Miniblog
* 豆邮 Doumail
* 日记 Note
* 相册 Album
* 图片 Photo
* 读书 Book
* 电影 Movie
* 音乐 Music
* 线上活动 Online
* 同城活动 Event
* 论坛 Discussion
* 回复 Comment
* 豆瓣猜 Guess
```

### 安装
```
pip install douban-client
```

或
```
easy_install douban-client
```

### 使用说明

#### OAuth 2.0 认证
```
from douban_client import DoubanClient

API_KEY = 'your api key'
API_SECRET = 'your api secret'

# 在 OAuth 2.0 中，
# 获取权限需要指定相应的 scope，请注意!!
SCOPE = 'shuo_basic_r,shuo_basic_w'

client = DoubanClient(API_KEY, API_SECRET, your_redirect_uri, SCOPE)

# 以下方式 2 选 1:
# 引导用户授权
print 'Go to the following link in your browser:' 
print client.authorize_url
code = raw_input('Enter the verification code:')
client.auth_with_code(code)

# 如果有之前有 token，则可以
client.auth_with_token(token)

```

至此，已经完成 OAuth 2.0 授权。

#### Douban API v2 说明
```
1. 豆瓣Api V2认证统一使用OAuth2
2. 数据返回格式统一使用json，GData不再使用
3. 需要授权的Api，需要加access_token的Header，并且使用https协议，限制具体见OAuth2文档
4. 不需要授权公开api可以使用http，参数里面如果不包含apikey的话，限制单ip每分钟10次
5. Api里面的通配符，:id代表纯数字， :name代表由数字+字母+[-_.]这些特殊字符
6. 使用HTTP Status Code表示状态
7. 列表参数使用start和count
8. POST/PUT 时中文使用UTF-8编码
9. 时间格式：yyyy-MM-dd HH:mm:ss, 如"2007-06-28 11:16:11"
```

#### 接口说明

默认参数（参考豆瓣官方文档）:
```
start: 0
count: 20
```
所有返回数据以豆瓣官方文档为准，各接口末尾处均有相应链接入口。


__用户 People__
```
# 以下 id 指用户数字 id
当前用户 client.people.me
指定用户 client.people.get(id) 
搜索用户 client.people.search(q)       # q: 搜索的关键词

# 此处是将广播关系接口放置到用户
关注用户 client.people.follow(id)
取消关注 client.people.unfollow(id)
粉丝信息 client.people.followers(id, start, count)
关注信息 client.people.following(id, start, count) 
关注关系 client.people.friendships(target_id, source_id) 
共同关注 client.people.follow_in_common(id, start,count) 
加入黑名单 client.people.block(id)
```
<http://developers.douban.com/wiki/?title=user_v2>

<http://developers.douban.com/wiki/?title=community_1_shuo#user_info>



__广播 Miniblog__
```
# 以下 id 指广播数字 id
当前用户Timeline client.miniblog.home_timeline(count)
指定用户Timeline client.miniblog.user_timeline(user_id, count)
@当前用户的广播  client.miniblog.mentions(count)

获取一条广播 client.miniblog.get(id)
新写一条广播 client.miniblog.new(text)
新写图片广播 client.miniblog.new(text, image=open('/path/pic.png'))
删除一条广播 client.miniblog.delete(id)

获取某广播回复列表 client.miniblog.comments(id)
回复某条广播       client.miniblog.comment.new(id, text)
获取某条广播回复   client.miniblog.comment.get(comment_id)
删除某条广播回复   client.miniblog.comment.delete(comment_id)

赞某广播 client.miniblog.like(id)
取消赞某广播 client.miniblog.unlike(id)
赞某广播用户列表 client.miniblog.likers(id)

转发广播 client.miniblog.reshare(id)
转发某广播的用户列表 client.miniblog.resharers(id)

```
<http://developers.douban.com/wiki/?title=community_1_shuo>



__豆邮 Doumail__
```
# 以下 id 指豆邮数字 id
# 豆邮发送过多会需要验证，请注意
获取一封豆邮 client.doumail.get(id)
新写一封豆邮 client.doumail.new(title, content, receiver_id)

标记一封豆邮 client.doumail.read(id)
批量标记豆邮 client.doumail.reads(ids) # ids 为 list

删除一封豆邮 client.doumail.delete(id)
批量删除豆邮 client.doumail.deletes(ids) # ids: [id, id, id]

豆邮收件箱列表 client.doumail.inbox(start, count)
豆邮发件箱列表 client.doumail.outbox(start, count)
未读豆邮列表   client.doumail.unread(start, count)

```
<http://developers.douban.com/wiki/?title=doumail_v2>



__日记 Note__
```
# 以下 id 指日记数字 id
# format: html_full, html_short, abstract, text，默认为text
获取一篇日记 client.note.get(id, format='text')
新写一篇日记 client.note.new(title, content)
更新一篇日记 client.note.update(title, content)
删除一篇日记 client.note.delete(id)

喜欢一篇日记     client.note.like(id)
取消喜欢一篇日记 client.note.unlike(id)

获取用户日记列表       client.note.list(user_id, start, count)
获取用户喜欢的日记列表 client.note.liked_list(user_id, start, count)

获取回复列表  client.note.comments(id, start, count)
新加一条回复  client.note.comment.new(id, content)
获取一条回复  client.note.comment.get(comment_id)
删除一条回复  client.note.comment.delete(comment_id)

```
<http://developers.douban.com/wiki/?title=doumail_v2>



__相册 Album__
```
# 以下 id 指相册数字 id
# desc 描述文字
获取一个相册 client.album.get(id)
新建一个相册 client.album.new(title, desc)
更新一个相册 client.album.update(id, title, desc)
删除一个相册 client.album.delete(id)

获取用户相册列表 client.album.list(user_id, start, count)
用户喜欢相册列表 client.album.liked_list(user_id, start, count)
获取相册图片列表 client.album.photos(id, start, count)

喜欢一个相册 client.album.like(id)
取消喜欢相册 client.album.unlike(id)

```
<http://developers.douban.com/wiki/?title=photo_v2#get_album>



__图片 Photo__
```
# 以下 id 指图片数字 id
获取一张图片 client.photo.get(id)
上传一张图片 client.photo.new(album_id, image) # image = open('/path/pic.png')
更新图片描述 client.photo.update(id, desc)     # desc 为描述文字
删除一条图片 client.photo.delete(id)

喜欢一张图片 client.photo.like(id)
取消喜欢图片 client.photo.unlike(id)

获取回复列表  client.photo.comments(id, start, count)
新加一条回复  client.photo.comment.new(id, content)
获取一条回复  client.photo.comment.get(comment_id)
删除一条回复  client.photo.comment.delete(comment_id)
```
<http://developers.douban.com/wiki/?title=photo_v2#get_photo>



__读书 Book__
```
# 以下 id 指图书条目数字 id
# q: 关键词, tag: 标签
获取一本图书信息 client.book.get(id)
通过isbn获取信息 client.book.isbn(isbn_number)
搜索图书信息     client.book.search(q, tag, start, count) 

获取图书标签 client.book.tags(id)
获取用户标签 client.book.tagged_list(user_id)

发表一条书评 client.book.review.new(id, title, content)
更新一条书评 client.book.review.update(review_id, title, content)
删除一条书评 client.book.review.delete(review_id)

```
<http://developers.douban.com/wiki/?title=book_v2>



__电影 Movie__
```
# 以下 id 指电影条目数字 id
# q: 关键词, tag: 标签
获取一部电影信息 client.movie.get(id)
通过imdb获取电影 client.movie.imdb(imdb_number)
搜索电影信息     client.movie.search(q, tag, start, count) 

获取电影标签 client.movie.tags(id)
获取用户标签 client.movie.tagged_list(user_id)

发表一条影评 client.movie.review.new(id, title, content)
更新一条影评 client.movie.review.update(review_id, title, content)
删除一条影评 client.movie.review.delete(review_id)

```
<http://developers.douban.com/wiki/?title=movie_v2>



__音乐 Music__
```
# 以下 id 指音乐条目数字 id
# q: 关键词, tag: 标签
获取音乐信息 client.music.get(id)
搜索音乐信息 client.music.search(q, tag, start, count) 

获取音乐标签 client.music.tags(id)
获取用户标签 client.music.tagged_list(user_id)

发表一条乐评 client.music.review.new(id, title, content)
更新一条乐评 client.music.review.update(review_id, title, content)
删除一条乐评 client.music.review.delete(review_id)

```
<http://developers.douban.com/wiki/?title=music_v2>



__线上活动 Online__
```
# 以下 id 指线上活动数字 id
# begin_time, end_time 格式为 '%Y-%m-%d %H:%M:%S'
# cate 可选值: day, week, latest
获取一条线上活动 client.online.get(id)
发表一条线上活动 client.online.new(title, desc, begin_time, end_time)
更新一条线上活动 client.online.update(title, desc, begin_time, end_time)
删除一条线上活动 client.online.delete(id)

参加一条线上活动 client.online.join(id)
取消参加线上活动 client.online.quit(id)

喜欢一条线上活动 client.online.like(id)
取消喜欢线上活动 client.online.unlike(id)

获取线上活动图片列表 client.online.photos(id, start, count)
上传图片到线上活动   client.online.upload(id, image) # image = open('xxx.jpg')

获取线上活动讨论列表 client.online.discussions(id, start, count)
在线上活动新发讨论   client.online.discussion.new(id, title, content)

获取参加线上活动成员列表 client.online.participants(id, start, count)

获取线上活动列表 client.online.list(cate, start, end) 
获取参加过的活动 client.online.joined(user_id, start, count)
获取组织过的活动 client.online.owned(user_id, start, count)

```
<http://developers.douban.com/wiki/?title=online_v2>



__同城活动 Event__
```
# 以下 id 指同城活动 id 
# q: 关键词, loc: 城市
# day_type: future, week, weekend, today, tomorrow
# type: all,music, film, drama, commonweal, salon, \
#       exhibition, party, sports, travel, others
获取同城活动 client.event.get(id)
搜索同城活动 client.event.search(q, loc, start, count)

参加同城活动 client.event.join(id)
取消参加活动 client.event.quit(id)

对同城活动感兴趣 client.event.wish(id)
取消同城活动兴趣 client.event.unwish(id)

某同城活动参加者   client.event.participants(id, start, count)
某同城活动感兴趣者 client.event.wishers(id, start, count)

获取用户创建过的同城活动 client.event.owned(user_id, start, count)
获取用户参加过的同城活动 client.event.participated(user_id, start, count)
获取用户感兴趣的同城活动 client.event.wished(user_id, start, count)

获取同城活动列表 client.event.list(loc, day_type, type, start, count)
```
<http://developers.douban.com/wiki/?title=event_v2>



__论坛 Discussion__
```
# 以下 id 指论坛帖子 id 
# target 指相应产品线（如 online, review 等）
# target_id 指相应产品 id
获取帖子 client.discussion.get(id)
发表帖子 client.discussion.new(target, target_id, title, content)
更新帖子 client.discussion.update(id, title, content)
删除帖子 client.discussion.delete(id)

获取帖子列表 client.discussion.list(target, target_id)

获取回复列表 client.discussion.comments(id, start, count)
新加一条回复 client.discussion.comment.new(id, content)
获取某条回复 client.discussion.comment.get(comment_id)
删除某条回复 client.discussion.comment.delete(comment_id)
```
<http://developers.douban.com/wiki/?title=discussion_v2>



__豆瓣猜 Guess__
```
# 这里是把分散日记，相册，线上活动猜放到一起了
猜你喜欢的日记      client.guess.notes(user_id)
猜你喜欢的相册      client.guess.albums(user_id)
猜你喜欢的线上活动  client.guess.onlines(user_id)
```
<http://developers.douban.com/wiki/?title=note_v2#get_rec_list>

<http://developers.douban.com/wiki/?title=photo_v2#album_guesses>

<http://developers.douban.com/wiki/?title=online_v2#guesslist>


已实现的接口中单元测试覆盖 90%+，如果文档中有没有说明的可以参考下： <https://github.com/liluo/douban-client/tree/master/tests>

### 联系
* 使用 douban-client 过程中遇到 bug, 可以到 [Issues](https://github.com/liluo/douban-client/issues) 反馈
* 比较紧急的问题可以在 Douban 或者 Twitter @liluoliluo 
* 欢迎提 pull request
