#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'

import pymysql

conn = pymysql.connect(host='10.0.2.63', port=3307, user='python', passwd='python', db='pystudy')

# cursor = conn.cursor()  #默认输出内容为元组类型

cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)   #输出内容改为字典类型

# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
#
# row_affected = cursor.execute("create table t1(id INT ,name VARCHAR(20))")
#
# row_affected=cursor.execute("INSERT INTO t1(id,name) values (1,'alvin'),(2,'xialv')")
#
# cursor.execute("update t1 set name = 'silv2' where id=2")

#查询数据
row_affected = cursor.execute("select * from t1")
one = cursor.fetchone()
cursor.scroll(-1,mode="relative")   # 相对当前位置移动
many = cursor.fetchmany(2)
cursor.scroll(0,mode='absolute')  # 相对绝对位置移动
allthing = cursor.fetchall()



conn.commit()
cursor.close()
conn.close()

print(one)
print(many)
print(allthing)