# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pymysql
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/index')
def index():

    user = ['wuyangjun', 'idjflajfl;a', 'fadfjakldj']

    return render_template("index.html", title="中国联通",  data_list=user)


@app.route('/add/user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'GET':
        return render_template("add_user.html")

    name = request.form.get('name')
    pwd = request.form.get('pwd')
    email = request.form.get('email')
    print(name, pwd, email)

    import pymysql
    conn = pymysql.connect(host='10.80.14.234', port=3306, user='root', password='123456', charset='utf8', db='db_ops')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    cursor.execute(
        "insert into tb_user(name, email, pwd,  depart_id) values('{}', '{}', '{}', 1)".format(name, email, pwd))

    conn.commit()

    cursor.close()
    conn.close()

    return "添加成功"


@app.route('/show/user')
def show_user():
    conn = pymysql.connect(host='10.80.14.234', port=3306, user='root', password='123456', charset='utf8', db='db_ops')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    cursor.execute("select * from tb_user")

    data_list = cursor.fetchall()
    # print(data_list)
    # for row in data_list:
    #     print(row)

    cursor.close()
    conn.close()

    return render_template('show_user.html', data_list= data_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
