# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f'{j}*{i}={i*j}',end="\t")
#     print()


# i=1
# while i<=9:
#     j = 1
#     while(j<=i):
#         print(f'{j}*{i}={i*j}',end="\t")
#         j=j+1
#     print()
#     i=i+1



# a=int(input('a='))
# for i in range (1,a+1):
#     for j in range(1,i+1):
#         print('*',end="\t")
#     print()


# a=int(input('a='))
# for i in range (1,a+1):
#     for j in range(1,i+1):
#         print(f'{j}',end='\t')
#     print()


# a=int(input('a='))
# for i in range(1,a+1):
#     for j in range(1,a+1):
#         if (j%2!=0 and i%2!=0) or (j%2==0 and i%2==0):
#             print('x',end='\t')
#         else:
#             print('y',end='\t')
#     print()
#
# (i+j)%2==0



# a=input('用户名a=')
# b=input('密码b=')
# A=('admin','zhangsan','taoge')
# B=('666888','123456','888666')
# if a=='' or b=='':
#     print('用户名和密码不能为空！')
# else:
#     for i in range (A):
#         for j in range (B):
#             if (b==j and a==i):
#                 print('登陆成功！')
#             else:
#                 print('输入错误，请重新输入！')
# 错误



# while True:
#     a=input('用户名a=')
#     b=input('密码b=')
#     if a=="" or b=='':
#         print('用户名和密码不能为空！')
#         continue
#     if (a=='admin' and b=='666888'):
#         print('登陆成功！')
#         break
#     elif (a=='zhangsan' and b =='123456'):
#         print('登陆成功！')
#         break
#     elif(a=='yangyiting' and b=='yyt'):
#         print('登陆成功！')
#         break


i=1
while i<=5:
    a = input('用户名a=')
    b=input('密码b=')
    if a == "" or b == '':
     print('用户名和密码不能为空！')
     i=i+1
     continue
    if (a == 'admin' and b == '666888'):
       print('登陆成功！')
       break
    elif (a=='zhangsan' and b =='123456'):
        print('登陆成功！')
        break
    elif(a=='yangyiting' and b=='yyt'):
        print('登陆成功！')
        break
    else:
        print('输入错误！请重新输入！')
        i = i+1
else:
    print('输入错误次数过多！已锁定！')