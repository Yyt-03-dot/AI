# i=0
# while i<10:
#     print('aaaaaa')
#     i=i+1
# else:
#     print('0')
# i=int(input("请输入i:"))
# while i-1>=0:
#     print('1111')
#     i=i-1
# else:
#     print(' ')

# i=int(input('请输入i='))
# total=0
# while i<=100:
#     if i%2==0:
#         total=total+i
#     i=i+1
#
# else:
#     print('输入错误')
# print(f'total={total}')
i=int(input('请输入i='))
total=0
if i<=100:
    while i<=100:
        if i%2==0:
            total=total+i
        i=i+1
    print(f'total={total}')
else:
    print('输入错误！')



