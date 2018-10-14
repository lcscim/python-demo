#__author__:asus
#date:2018/10/14
import pymysql

def get_list(req):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(req)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
def get_one(req,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(req,args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def set_list(req,args):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='s4db65', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute(req,args)
    conn.commit()
    cursor.close()
    conn.close()