class Car:
    wheel=4#类属性，共享
    def __init__(self,c_color,c_brand,c_name,c_price):
        #实例属性
        self.color=c_color
        self.c_brand=c_brand
        self.c_name=c_name
        self.c_price=c_price
        print('添加完毕')
    def running(self):
        print(f'{self.c_name}正在运行中')
    def total_price(self,discount,rate):
        total_price=self.c_price*discount+rate*self.c_price
        return total_price
    def __str__(self):
        return f'{self.color},{self.c_brand},{self.c_name},{self.c_price}'
    def __eq__(self,other):
        if not(isinstance(other,Car)):
            return False
        return self.color==other.color and self.c_brand==other.c_brand and self.c_name==other.c_name and self.c_price==other.c_price
    def __lt__(self,other):
        return self.c_price<other.c_price
c1=Car('红色','AAAA','yangyiting',10001)
print(c1)
print(c1.c_brand)
print(c1.wheel)
print(Car.wheel)
# c1.running()
# print(c1.total_price(discount=2,rate=3))
c2=Car('红色','AAAA','yangyiting',1000)
print(c2)
print(c1==c2)
print(c1>c2)