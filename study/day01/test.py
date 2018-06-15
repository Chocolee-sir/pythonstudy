#!/usr/bin/env python
# encoding:utf-8
__author__ = 'Chocolee'

#print('hello world!')


'''
data = {'liyiliang': '123456', 'root': 'root'}
num = 0
while True:
    user = input('请输入用户名：')
    if user in data.keys():
        while True:
            password = input('请输入密码：')
            if password == data[user]:
                print('%s 登陆成功~~~' % user)
                exit()
            else:
                num = num + 1
                if num < 3:
                    print('%s 登录密码错误，请重新输入！！！您已经输入%s次错误！！' % (user, num))
                    continue
                else:
                    print('输入错误次数为%s次，错误次数上限，bye bye~~~' % num)
                    exit()
    else:
        print('%s 用户名不存在，请重新输入。' % user)
'''


'''
num = 1
while num < 11:
    print(num)
    num = num + 1
'''
'''
n1 = 'liyiliang'
n2 = 'nb,'

n3 = n2 * 5
print(n3)


import timeit

def while_one():
    i = 0
    while 1:
        i += 1
        if i == 10000000:
            break

def while_true():
    i = 0
    while True:
        i += 1
        if i == 10000000:
            break

if __name__ == "__main__":
    w1 = timeit.timeit(while_one, "from __main__ import while_one", number=3)
    wt = timeit.timeit(while_true, "from __main__ import while_true", number=3)
    print("while one: %s\nwhile_true: %s" % (w1, wt))
'''

'''
num = 1
while num < 11:
    if num == 7:
        num += 1
        continue
    print(num)
    num += 1
'''

'''
num = 0
a = 0
while num < 101:
    num+=1
    a = a + num
print(a)
'''

'''
num = 1
while num <100:
    if num % 2 != 0:
        print(num)
    num += 1
'''

'''
num = 1
while num <101:
    if num % 2 == 0:
        print(num)
    num += 1
'''