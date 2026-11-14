s1='123\n45'
s2='\t67890''ok'
print(s1)
print(s2)
print(s1+s2)
print(s1+','+s2)


name='Yang'
age=20
skill='哈哈哈'
hobby='python'
print("大家好，我是"+name+"，今年"+str(age)+"岁，学习的专业是"+skill+"，爱好"+hobby)

name='Yang'
age=20
skill='哈哈哈'
hobby='python'
print("大家好，我是  %s，今年%s岁，学习的专业是%s，爱好%s"%(name,age,skill,hobby))

name='Yang'
age=20
skill='哈哈哈'
hobby='python'
print(f"大家好，我是{name}，今年{age}岁，学习的专业是{skill}，爱好{hobby}")