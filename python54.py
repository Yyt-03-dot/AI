

print('''
########购物车系统########
#      1.添加购物车      #
#      2.修改购物车      #
#      3.删除购物车      #
#      4.查询购物车      #
#      5.退出购物车      #
#########################
''')
cart={}
while True:
    choice=input('请选择要执行的操作(1-5)')

    match choice:
        case '1':
            name1=input('请输入商品的名称')
            if name1 not in cart:
                price1 = float(input('请输入商品的价格'))
                num1 = int(input('请输入商品的数量'))
                g={name1:(price1,num1)}
                cart[name1]=(price1,num1)
                print(f'录入成功！购物车商品为：{name1},价格为{price1},数量为{num1}')
            else:
                print('商品已经存在，请重新选择！')
        case '2':
            if cart=={} :
                print('购物车为空！')
            else:
                name2 = input('请输入要修改的商品的名称')
                price2 = float(input('请输入商品的价格'))
                num2 = int(input('请输入商品的数量'))
                cart[name2]=(price2,num2)
                print(f'修改成功！购物车商品为：{name2},价格为{price2},数量为{num2}')
        case '3':
            if cart == {}:
                print('购物车为空！')
            else:
                name3 = input('请输入要删除的商品的名称')
                if name3 in cart:
                    del cart[name3]
                    print('删除成功！')
                else:
                    print('商品不存在！')
        case '4':
            if cart == {}:
                print('购物车为空！')
            else:
                for name4 in cart:
                    b,c=cart[name4]
                    print(f'商品名称：{name4}\t，商品价格：{b}\t，商品数量：{c}\t')

        case '5':
            print('退出成功！')
            break
        case _:
             print('输入不合法！')


