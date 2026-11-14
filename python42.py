# num_list=[]
# for i in range(1,21):
#     num=i**2
#     num_list.append(num)
# print(num_list)
# num_list3=[i**2 for i in range(1,21)]
# print(num_list3)
#
# num_list2=[19,23,54,64,87,20,109,232,123,43,26,55,72]
# new_list=[]
# for y in num_list2:
#     if y% 2==0:
#         z=y**2
#         new_list.append(z)
# print(new_list)
# num_list4=[i**2 for i in num_list2 if i%2==0]
# print(num_list4)
#
# list1=['M','A','D','F','V']
# list2=['A','B','C','D','E']
# list3=['w','F','J']
# list=list1+list2+list3
# print(list)
# new_list=[]
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
#         new_list.sort()
# print(new_list)

num_list=[]
for i in range(10):
    a=input('请输入一个字符串')
    b=a[::-1]
    b=b.upper()
    num_list.append(b)
for num in num_list:
    print(num)




