f=open("D:/apikey.txt",'r',encoding='utf-8')
content=f.read()
print(content)
f.close()
with open("D:/apikey.txt",'w',encoding='utf-8') as f:
