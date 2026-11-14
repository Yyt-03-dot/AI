# def jc(n):
#     if n==0:
#         return 1
#     else:
#         return n*jc(n-1)
# result=jc(10)
# print(result)

def case(*args,discount=0,points=0,shipping_fee=0):
    couse=0
    num1=0
    num2=0
    for i in args:
        jine=i[1]*i[2]
        couse+=jine

    if couse>discount and couse>=5000:
        num1=discount
    if  couse >= 5000 and points//100<couse:
        num2=points//1000
    num3=couse-num1-num2+shipping_fee
    return num3



