# coding:utf-8
import requests
import pymysql
from lxml import html
k = 1
for i in range(10):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(i*25)
    con = requests.get(url).content
    sel = html.fromstring(con)
    # 所有的信息都在class属性为info的div标签里，可以先把这个节点取出来 //*[@id="content"]/div/div[1]/ol
    for i in sel.xpath('//div[@class="info"]'):

        # 影片名称
        title = i.xpath('div[@class="hd"]/a/span[@class="title"]/text()')[0]
        #print(title)
        info = i.xpath('div[@class="bd"]/p[1]/text()')
        # 导演演员信息
        info_1 = info[0].replace(" ", "").replace("\n", "")
        # 上映日期
        date = info[1].replace(" ", "").replace("\n", "").split("/")[0]
        # 制片国家
        country = info[1].replace(" ", "").replace("\n", "").split("/")[1]
        # 影片类型
        geners = info[1].replace(" ", "").replace("\n", "").split("/")[2]
        # 评分
        rate = i.xpath('//span[@class="rating_num"]/text()')[0]
        # 评论人数
        comCount = i.xpath('//div[@class="star"]/span[4]/text()')[0]

        # 打印结果看看
        print ("TOP%s" % str(k))
        print( title, info_1, rate, date, country, geners, comCount )


        connection=''
        try:
            # 获取一个有效的数据库连接对象，此处填写你的数据库信息，特别注意charset一定要写成'utf8'，不能写成'utf-8'。
            connection = pymysql.connect(host='localhost', port=3306,
                                         user='zhao153195', password='zhao153195',
                                         db='crawl', charset='utf8')
            if connection:
                print("[mysql]>>正确获取数据库的连接对象")

            # 创建一个游标对象
            curosr = connection.cursor()
            print('[mysql]正确获取游标对象')
            # 设置插入数据的sql语句模板
            sql = "insert into doubanmovie VALUES (null,'%d','%s','%s,','%s','%s','%s','%s')" % (k, title, rate, comCount, date, country, info_1)
            print('[mysql]>>%s' % sql)

            # 使用游标对象发送sql语句并将服务器结果返回
            affectedRows = curosr.execute(sql)
            msg = '[mysql]>>写入操作成功' if affectedRows > 0 else '[mysql]>>写入失败'
            print(msg)
            # 事务提交
            connection.commit()
            print("[mysql]>>事务提交")
        except:
            connection.rollback()
            print('[mysql]事务回滚')
        finally:
            # 关闭数据库连接
            connection.close()
            print("[mysql]>>关闭数据库连接")
            k += 1
