import pymysql
conn = pymysql.connect(host='10.80.14.234', port=3306, user='root', password='123456', charset='utf8', db='db_ops')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


cursor.execute("select * from tb_user")

data_list = cursor.fetchall()
print (data_list)

print("dainfdaidn ")
for row in data_list:
    print (row)

cursor.close()
conn.close()
