# score=int(input('请输入你的分数：'))
# if score>=680:
#     print('''欢迎您来清华读书
#     ddddd''')
# else:
#     print('呵呵')
# # print('----------------')
#
# a=int(input('账号：'))
# b=int(input('密码：'))
# c=123456
# d=7890
# if a==c and b==d:
#     print('输入正确，成功登录！')
#
# else:
#     print('输入不正确！登录失败！')


# year=int(input('请输入年份：'))
# if (year%100!=0 and year%4==0) or (year%400==0):
#     print(f'{year}年是闰年')
# else:
#     print(f'{year}年是平年')

# num=int(input('请输入一个数字：'))
# if num%2!=0:
#     print(f'数字{num}是奇数')
# if num%2==0:
#     print(f'数字{num}是偶数')
#
# age=int(input('请输入你的年龄：'))
# if age>=18:
#     print('你已成年')
# else:
#     print('你未成年')

#
# num=int(input('请输入一个数字：'))
# if num>0:
#     print('zhengshu')
# elif num==0:
#     print('zero')
# else:
#     print('fushu')

#
# a=input('账号：')
# b=input('密码：')
# if a=='admin' and b=='666888':
#     print('登录成功！')
# elif a=='root' and b=='547527':
#     print('登录成功！')
# elif a=='yyy' and b=='123456':
#     print('登录成功！')
# else:
#     print('登陆失败！')
# if (a,b)in [('admin','666888'),('root','547527')-------    ]
#     print('登录成功！')



# a=int(input('a'))
# b=int(input('b'))
# c=int(input('c'))
# if (a+b<c or b+c<a or a+c<b):
#     print('不能构成三角形')
# elif (a+b>c and b+c>a and a+c>b) and a==b==c:
#     print('等边三角形')
# elif (a+b>c and b+c>a and a+c>b) and (a==b!=c or b==c!=a or a==c!=b):
#     print('等腰三角形')
# else:
#     print('普通三角形')
# a=int(input('a'))
# b=int(input('b'))
# c=int(input('c'))
# if (a+b>c and a+c>b and b+c>a):
#     if a==b==c:
#         print('等边三角形')
#     elif a==b or b==c or a==c:
#         print('等腰三角形')
#     else:
#         print('普通三角形')
# else:
#     print('不能构成三角形')

num=float(input('yongdianliang:'))
if num<2880:
    cost=num*0.4883
    print(f'电价为{cost}yuan')
elif 2880<=num<=4800:
    cost=num*0.5383
    print(f'电价为{cost}yuan')
else:
    cost=num*0.7883
    print(f'电价为{cost}yuan')

