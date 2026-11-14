# def S(a,h):
#     s=a*h/2
#     return s
#
# a=S(1,2)
# print(a)



# def yuanyin(a):
#     num=0
#     for i in a:
#         if i in 'a,e,i,o,u,A,E,I,O,U':
#             num+=1
#     return num
#
# num1=yuanyin('asdfghjkleee')
# print(num1)

# def score(list):
#     max_s=max(list)
#     min_s=min(list)
#     avg_s=round(sum(list)/len(list),1)
#     return max_s,min_s,avg_s
#
# s_score=[10,22,4,60,77,99,100 ]
# maxs,mins,avgs=score(s_score)
# print(maxs,mins,avgs)
#


# def h(score):
#     if score>=90:
#         return 'A'
#     if score>=75:
#         return 'B'
#     if score>=60:
#         return 'C'
#     else:
#         return 'D'
#
# print(h(3))


# def huiwen(a):
#     listnum=[]
#     for i in a:
#         listnum.append(i)
#     num_list2=listnum[::-1]
#     if listnum==num_list2:
#         return True
#     else:
#         return False
#
#
# print(huiwen('12345432'))


# def time(a):
#     hour=a/3600
#     min=a/60
#     return hour,min
#
# hour,min=time(3600)
# print(hour,min)

def triangle(a,b,c):
    if a+b>c and b+c>a and c+a>b:
        if a==b==c:
            return '等边三角形'

        elif a==b or b==c or c==a:
            return '等腰三角形'

        else:
            return '普通三角形'
    else:
        return '不能构成三角形'

triangle1=triangle(3,2,1)
print(triangle1)