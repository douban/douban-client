### douban-client

douban-client 是对豆瓣 API v2 接口进行了一个简单封装，主要包括了 OAuth 2.0 认证、图片上传以及接口方面的调用。

目前已完成的接口有：
``` 
* 用户 People
* 广播 Miniblog
* 豆邮 Doumail
* 日记 Note
* 相册 Album
* 图片 Photo
* 线上活动 Online
* 讨论区 Discussion
```

正在进行开发中的接口有:
```
* 豆瓣猜 Guess
* 同城活动 Event
* 音乐 Music
* 电影 Movie
* 图书 Book
* 回复 Comment
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
在 OAuth 2.0 中，权限

#### 接口说明

通用接口:
```
获取 client.xxx.get()
新建 client.xxx.new()
更新 client.xxx.update()
删除 client.xxx.delete()
列表 client.xxx.list()
```

默认参数（参考豆瓣官方文档）:
```
start: 0
count: 20
```

__用户 People__
```
# 以下 id 部分指用户数字 id
当前用户 client.people.me
指定用户 client.people.get(id) 
搜索用户 client.people.search(q)       # q: 搜索的关键词

关注用户 client.people.follow(id)
取消关注 client.people.unfollow(id)
粉丝信息 client.people.followers(id, start, count)
关注信息 client.people.following(id, start, count) 
关注关系 client.people.friendships(target_id, source_id) 
共同关注 client.people.follow_in_common(id, start,count) 
加入黑名单 client.people.block(id)
```

__广播 Miniblog__
```
```



已实现的接口中单元测试覆盖超过 90%，如果文档中有没有说明的可以参考下： <https://github.com/liluo/douban-client/tree/master/tests>

### 联系
* 使用 douban-client 过程中遇到 bug, 可以到 [Issues](https://github.com/liluo/douban-client/issues) 反馈
* 比较紧急的问题可以在 Douban 或者 Twitter @liluoliluo 
* 欢迎提 pull request
