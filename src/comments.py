# encoding:UTF-8
import pymysql,re,time,requests,urllib.request
from collections import OrderedDict

weibo_id = input('输入单条微博ID：')
#url='https://m.weibo.cn/single/rcList?format=cards&id=4182683255025485'  + '&type=comment&hot=1&page={}'#爬热门评论
url='https://m.weibo.cn/api/comments/show?id='+ weibo_id + '&page={}' #爬时间排序评论
headers = {
    'Host' : 'm.weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Referer' : 'https://m.weibo.cn/status/'+weibo_id,
    'Cookie': 'Your cookies',  # Your cookies
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
    'Connection' : 'keep-alive',
    }
i = 0
comment_num = 1
while True:
    # if i%2==0:     #26-31行 爬热门评论
    #     r = requests.get(url = url.format(i),headers = headers)
    #     print(r)
    #     comment_page = r.json()[1]['card_group']
    # else:
    #     r = requests.get(url = url.format(i),headers = headers)
    #     print(r)
    #     comment_page = r.json()[1]['card_group']

    # 抓取的评论数
    if comment_num-1 == 10000:
        print("抓取了10000条记录,结束")
        break
    r = requests.get(url = url.format(i),headers = headers)  #32-33行 爬时间排序评论

    if r.status_code ==200:
        try:
            comment_page = r.json()['data']['data']
            print('正在读取第 %s 页评论：' % i)
            for j in range(0,len(comment_page)):
                print('第 %s 条评论' % comment_num)
                user = comment_page[j]
                comment_id = user['user']['id']
                print(comment_id)
                user_name = user['user']['screen_name']
                print(user_name)
                created_at = user['created_at']
                print(created_at)
                # emoji过滤
                text = re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]','',user['text'])
                print(text)
                likenum = user['like_counts']
                print(likenum)
                source = re.sub('[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]','',user['source'])
                print(source + '\r\n')
                conn =pymysql.connect(host='127.0.0.1',user='root',password='Your Password',charset="utf8",use_unicode = False)    #连接服务器
                cur = conn.cursor()
                sql = "insert into nlp.masu(comment_id,user_name,created_at,text,likenum,source) values(%s,%s,%s,%s,%s,%s)"
                param = (comment_id,user_name,created_at,text,likenum,source)
                print(param)
                try:
                    A = cur.execute(sql,param)
                    conn.commit()
                except Exception as e:
                    print(e)
                    conn.rollback()
                comment_num+=1
            i+=1
            time.sleep(4)
        except Exception as ex:
            print(ex)
            i+=1
            pass
    else:
        break