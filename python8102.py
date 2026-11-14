#商品
class Goods:
    def __init__(self,name,price,num):
        self.name=name
        self.price=price
        self.num=num
    def __str__(self):
        return f'商品名称{self.name},商品价格{self.price},商品数量{self.num}'
    def revise_goods(self,price=None,num=None):
        if price is not None:
            self.price=price
        if num is not None:
            self.num=num
#购物车系统
class ShoppingCart:
    def __init__(self):
        self.good_list=[]
    def add_goods(self):
        name=input('请输入要投喂的商品名称喵：')
        for good in self.good_list:
            if  good.name==name:
                print('商品已经存在了喵！')
                return
        price=float(input('请输入要投喂的商品价格喵：'))
        num=int(input('请输入要投喂的商品数量喵：'))
        good=Goods(name,price,num)
        self.good_list.append(good)
        print('投喂成功喵！感谢大人投喂~')
    def revise_goods(self):
        name1=input('请输入要修改的商品名称喵：')
        for good in self.good_list:
            if  good.name==name1:
                print(f'当前商品信息为{good}')
                price = float(input('请输入要修改的商品价格喵：'))
                num = int(input('请输入要修改的商品数量喵：'))
                good.revise_goods(price,num)
                print(f'修改成功！当前商品信息为{good}')
                return
        print('商品不存在喵！请先投喂商品喵~')
    def delete_goods(self):
        name1 = input('请输入要删除的商品名称喵：')
        for good in self.good_list:
            if  good.name==name1:
                self.good_list.remove(good)
                print('删除成功了喵~呜呜TvT')
                return
        print('商品不存在喵！请先投喂商品喵~')
    def show_goods(self):
        if len(self.good_list)==0:
            print('购物车空空如也呢！欢迎投喂商品喵~')
        for good in self.good_list:
            print(good)
    def run_cart(self):
        while True:
            print('欢迎访问购物车系统！')
            print(r'       /\                              /\                ')
            print("---------------------------------------------------------")
            print('|   1.添加商品 2.修改商品 3.删除商品 4.查询商品 5.退出购物车   |')
            print("---------------------------------------------------------")
            choice=int(input('请输入要执行的操作：'))
            match choice:
                case 1:
                    self.add_goods()
                case 2:
                    self.revise_goods()
                case 3:
                    self.delete_goods()
                case 4:
                    self.show_goods()
                case 5:
                    print('退出成功！欢迎下次光临！')
                    break
                case _:
                    print('输入不合法喵！请输入正确的数字喵')

if __name__=='__main__':
    goods=ShoppingCart()
    goods.run_cart()