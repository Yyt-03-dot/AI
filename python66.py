# def cala_data(*args,**kwargs):
#     min_data=min(*args)
#     max_data=max(*args)
#     avg_data=sum(args)/len(args)
#     if 'round' in kwargs:
#         avg_data=round(avg_data,kwargs['round'])
#     if print is True:
#         print(min_data,max_data,avg_data)
#     return min_data,max_data,avg_data
#
# print(cala_data(3,200,55,88,99.111,round=1))

# def add(x,y):
#     return x+y
# def subtract(x,y):
#     return x-y
# def clac(x,y,oper):
#     return oper(x,y)
# result=clac(10,20,add)
# print(result)


# a=lambda:print('---------')
# a()
#
# def add(a,b):
#     return a+b
# print(add(1,2))
#
# add1=lambda a,b:a+b
# print(add1(1,2))


def length(*args):
    a=sorted(args,key=len)
    return a

data_list=['aadwd','wdAdd','www','qqq','a']
print(length(*data_list))



skll=lambda list1:sorted(list1,key=len)
data_list1=['aadwd','wdAdd','www','qqq','a']
print(skll(data_list1))