name=input('请输入你的姓名：')
age=input('请输入你的年龄：')
print(f'你的姓名是{name}，你的年龄是{age}岁')


money=10000
code=input('请输入密码:')
change=input('输入取款金额：')
remain=money-int(change)
print(f'你的余额为{remain}元')
print(f'你的余额为{money-int(change)}元')

a=input('请输入你的第一个数字：')
b=input('请输入你的第二个数字：')
print(f'他们的和为{int(a)+int(b)}')