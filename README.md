
## 获取评论
  
  参考[博客](https://www.tuicool.com/articles/ZN3EjuB),使用来爬去移动端的评论，在控制台查看到的信息如下：
  
  ```xml
  
   Request URL:https://m.weibo.cn/api/comments/show?id=4194386432506328&page=1
   Request Method:GET
   Status Code:200 OK
   Remote Address:180.149.153.242:443
   Referrer Policy:no-referrer-when-downgrade

  ```
 
 参数只有两个
 
 ```xml
 id:4194386432506328
 page:1
 ```

 而返回的结果为
 
 ```json
{
    "ok": 1, 
    "msg": "数据获取成功", 
    "data": {
        "data": [
            {
                "id": 4194389259388425, 
                "created_at": "3分钟前", 
                "source": "vivo智能手机", 
                "user": {
                    "id": 3067934241, 
                    "screen_name": "篮球特训营", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/crop.0.0.2048.2048.180/b6dcf621ly8fm9g304u1pj21kw1kwgny.jpg", 
                    "verified": true, 
                    "verified_type": 0, 
                    "verified_type_ext": 0, 
                    "mbtype": 12, 
                    "profile_url": "https://m.weibo.cn/u/3067934241?uid=3067934241&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/d_doge-d903433c82.png\" style=\"width:1em;height:1em;\" alt=\"[doge]\"></span>我置顶微博在送欧文4，要参加吗", 
                "like_counts": 2, 
                "liked": false
            }, 
            {
                "id": 4194388755709337, 
                "created_at": "5分钟前", 
                "source": "iPhone客户端", 
                "user": {
                    "id": 1892592753, 
                    "screen_name": "CrazyHAO-inter", 
                    "profile_image_url": "https://tva2.sinaimg.cn/crop.0.8.750.750.180/70ceac71jw8fc6ushk9slj20ku0lajs1.jpg", 
                    "verified": true, 
                    "verified_type": 0, 
                    "verified_type_ext": 0, 
                    "mbtype": 0, 
                    "profile_url": "https://m.weibo.cn/u/1892592753?uid=1892592753&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_yinxian-b3257f06bb.png\" style=\"width:1em;height:1em;\" alt=\"[阴险]\"></span>约老师来火箭组个“三巨头”三人场均30个助攻", 
                "like_counts": 0, 
                "liked": false
            }, 
            {
                "id": 4194388722794960, 
                "created_at": "5分钟前", 
                "source": "iPhone客户端", 
                "user": {
                    "id": 2783031803, 
                    "screen_name": "游二逍遥", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/default/images/default_avatar_male_180.gif", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 0, 
                    "profile_url": "https://m.weibo.cn/u/2783031803?uid=2783031803&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "看了一场比赛就欣赏他了。有时候打球的智商不是练出来的，这是天分", 
                "like_counts": 0, 
                "liked": false
            }, 
            {
                "id": 4194388534438170, 
                "created_at": "6分钟前", 
                "source": "魅族轻巧旗舰 PRO 6", 
                "user": {
                    "id": 5165691822, 
                    "screen_name": "王闰恩泽", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/crop.0.0.996.996.180/005DAIq2ly8fgk0m164sij30ro0ro7a5.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 2, 
                    "profile_url": "https://m.weibo.cn/u/5165691822?uid=5165691822&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "要不是傻库把约老师怼了出去<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_yunbei-c6964bf237.png\" style=\"width:1em;height:1em;\" alt=\"[允悲]\"></span>，这场真不好说", 
                "like_counts": 0, 
                "liked": false
            }, 
            {
                "id": 4194387686652218, 
                "created_at": "10分钟前", 
                "source": "荣耀9 美得有声有色", 
                "user": {
                    "id": 3479902943, 
                    "screen_name": "默菲与默里", 
                    "profile_image_url": "https://tvax1.sinaimg.cn/crop.0.0.996.996.180/cf6b1adfly8fn0waxixklj20ro0ro76l.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 0, 
                    "profile_url": "https://m.weibo.cn/u/3479902943?uid=3479902943&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "回复<a href='https://m.weibo.cn/n/大妹子bb小ks5'>@大妹子bb小ks5</a>:帮忙点击了举报，妹子不用谢。", 
                "reply_id": 4194387401239009, 
                "reply_text": "刺激过头、把黄瓜断了半截在bb里面了、好尴尬、求亲们出下主意帮帮我eoe", 
                "like_counts": 0, 
                "liked": false
            }, 
            {
                "id": 4194387607072949, 
                "created_at": "10分钟前", 
                "source": "iPhone客户端", 
                "user": {
                    "id": 5207771154, 
                    "screen_name": "绿帽检测顾问cha159875", 
                    "profile_image_url": "https://tvax3.sinaimg.cn/crop.0.0.512.512.180/005GrhaWly8fn5navwnm8j30e80e8jrp.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 0, 
                    "profile_url": "https://m.weibo.cn/u/5207771154?uid=5207771154&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_keai-9f81f72301.png\" style=\"width:1em;height:1em;\" alt=\"[可爱]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_keai-9f81f72301.png\" style=\"width:1em;height:1em;\" alt=\"[可爱]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_keai-9f81f72301.png\" style=\"width:1em;height:1em;\" alt=\"[可爱]\"></span>你的老公出轨过吗~~~~~<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/default/d_heng-5670fca4fa.png\" style=\"width:1em;height:1em;\" alt=\"[哼]\"></span>~~~你的妻子背叛过吗~~~~<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/d_xiongmao-3891cc9e79.png\" style=\"width:1em;height:1em;\" alt=\"[熊猫]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/d_xiongmao-3891cc9e79.png\" style=\"width:1em;height:1em;\" alt=\"[熊猫]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/d_xiongmao-3891cc9e79.png\" style=\"width:1em;height:1em;\" alt=\"[熊猫]\"></span>绿帽检测员帮到你<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/w_taiyang-eebe0749ad.png\" style=\"width:1em;height:1em;\" alt=\"[太阳]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/w_taiyang-eebe0749ad.png\" style=\"width:1em;height:1em;\" alt=\"[太阳]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/w_taiyang-eebe0749ad.png\" style=\"width:1em;height:1em;\" alt=\"[太阳]\"></span>dicjdnb", 
                "like_counts": 0, 
                "liked": false
            }, 
            {
                "id": 4194387498408536, 
                "created_at": "10分钟前", 
                "source": "OPPO智能手机", 
                "user": {
                    "id": 2950670373, 
                    "screen_name": "上将军孙膑", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/crop.0.0.664.664.180/afdfa825ly8fkxqbc4tvuj20ig0igjsv.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 2, 
                    "profile_url": "https://m.weibo.cn/u/2950670373?uid=2950670373&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "曾经周老师打败过的男人", 
                "like_counts": 0, 
                "liked": false
            }, 
            {
                "id": 4194387472417278, 
                "created_at": "10分钟前", 
                "source": "iPhone客户端", 
                "user": {
                    "id": 6200551947, 
                    "screen_name": "用户6200551947", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/crop.0.0.512.512.180/006LCSOnly8fn0c1f6wdkj30e80e8aae.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 2, 
                    "profile_url": "https://m.weibo.cn/u/6200551947?uid=6200551947&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "买🏀鞋 找 我<span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span><span class=\"url-icon\"><img src=\"//h5.sinaimg.cn/m/emoticon/icon/others/l_xin-8e9a1a0346.png\" style=\"width:1em;height:1em;\" alt=\"[心]\"></span>", 
                "like_counts": 1, 
                "liked": false
            }, 
            {
                "id": 4194387401239009, 
                "created_at": "11分钟前", 
                "source": "iPhone客户端", 
                "user": {
                    "id": 3238860294, 
                    "screen_name": "大妹子bb小ks5", 
                    "profile_image_url": "https://tvax3.sinaimg.cn/crop.0.0.960.960.180/c10d1606ly8fnaltbkgcmj20qo0qotaj.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 0, 
                    "profile_url": "https://m.weibo.cn/u/3238860294?uid=3238860294&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "刺激过头、把黄瓜断了半截在bb里面了、好尴尬、求亲们出下主意帮帮我eoe", 
                "like_counts": 0, 
                "liked": false
            }, 
            {
                "id": 4194387313796866, 
                "created_at": "11分钟前", 
                "source": "三星 Galaxy S7 Edge", 
                "user": {
                    "id": 5854152462, 
                    "screen_name": "吴焊三", 
                    "profile_image_url": "https://tvax4.sinaimg.cn/crop.0.0.996.996.180/006obqtUly8fk7okhzrq0j30ro0rodhr.jpg", 
                    "verified": false, 
                    "verified_type": -1, 
                    "mbtype": 2, 
                    "profile_url": "https://m.weibo.cn/u/5854152462?uid=5854152462&luicode=20000061&lfid=4194386432506328", 
                    "remark": "", 
                    "following": false, 
                    "follow_me": false
                }, 
                "text": "约老师典型的欧洲型中锋，技术全面。。。。能投能传，能抢篮板能策应挡拆。。。", 
                "like_counts": 0, 
                "liked": false
            }
        ], 
        "total_number": 19, 
        "max": 2
    }
}

```

可以直接获取到评论信息

而打开第二页发现请求为：

```xml
Request URL:https://m.weibo.cn/api/comments/show?id=4194386432506328&page=2
Request Method:GET
Status Code:200 OK
Remote Address:180.149.153.242:443
Referrer Policy:no-referrer-when-downgrade

```

确认 参数 id 为此篇博文对应的id，而page则为评论页数。

使用request请求返回JSON串再解析。
循环解析到数据库，使用jieba分词，使用SnowNPL分析情感。

## 注意

- 为了防止weibo后台爬虫检测，所有每读取一页线程sleep(3)  

- 可能weibo做了反爬虫策略，中途返回的某些页可能数据为空，所以解析会出现异常，处理方法为捕捉异常判断后继续处理。

