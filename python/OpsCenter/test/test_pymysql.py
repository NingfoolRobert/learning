import pymysql
conn = pymysql.connect(host='10.80.14.234', port=3306, user='root', password='123456', charset='utf8', db='db_ops')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


cursor.execute("insert into tb_user(name, email, pwd,  depart_id) values('nbf', 'beifei.ning@cicc.com.cn', '123456', 1)")

conn.commit()

cursor.close()
conn.close()
