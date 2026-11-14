a_list=[]
for i in range(10):
    a=int(input("请输入一个数字"))
    a_list.append(a)
print(a_list)
a_list.sort()
print(a_list)
print(f'{a_list[0]}')
print(f'{a_list[-1]}')
print(sum(a_list)/len(a_list))




