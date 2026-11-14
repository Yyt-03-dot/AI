try:
    my_name=int(input('请输入你的姓名'))
    print('---------------')
    print(my_name)
    print('---------------')
except ValueError as e:
    print('程序错误',e)
finally:
    print('aaaa')