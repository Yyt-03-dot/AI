# import random
# i=random.randint(1,10)
# while True:
#     a = int(input('a='))
#     if i>a:
#         print("猜小了！")
#         continue
#     elif i<a:
#         print('猜大了！')
#         continue
#     else :
#         print('正确！')
#         break
#
# total=0
# for i in range(1,1001):
#     if i%5==0:
#         total=total+i
# print(total)


a=input('字符串为')
char_a=0
char_k=0
for i in a:
    if i=='a':
        char_a=char_a+1
    if i =='k':
        char_k=char_k+1
print(char_a)
print(char_k)

