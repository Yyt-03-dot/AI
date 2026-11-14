

#学生成绩
class Student:
    def __init__(self,name,chinese,math,english):
        self.name=name
        self.chinese=chinese
        self.math=math
        self.english=english
    def __str__(self):
        return f'{self.name}:语文{self.chinese}|数学{self.math}|英语{self.english}|总分{self.chinese+self.english+self.math}'
    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese=chinese
        if math is not None:
            self.math=math
        if english is not None:
            self.english=english
#教务管理系统
class EduManagement:
    system_version='1.0'
    system_name='Edu'
    def __init__(self):
        self.student_list=[]
    def add_student(self):
        name=input('请输入学生姓名')
        for s in self.student_list:
            if s.name==name:
                print('学生已经存在，添加失败！')
                return
        chinese=int(input('请输入学生语文成绩'))
        math=int(input('请输入学生数学成绩'))
        english=int(input('请输入学生英语成绩'))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu=Student(name,chinese,math,english)
            self.student_list.append(stu)
            print('添加成功！')
        else:
            print('成绩不合法！')
    def update_student(self):
        name1=input('请输入要修改的学生姓名')
        for s in self.student_list:
            if s.name==name1:
                print(f'当前成绩为{s}')
                chinese = int(input('请输入学生语文成绩'))
                math = int(input('请输入学生数学成绩'))
                english = int(input('请输入学生英语成绩'))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    s.update_score(chinese,math,english)
                    print(f'修改成功！学生成绩为{s}')
                    return
                else:
                    print('成绩不合法！')
                    return
        print('学生信息不存在！')
    def del_student(self):
        name1 = input('请输入要删除成绩的学生姓名')
        for s in self.student_list:
            if s.name == name1:
                self.student_list.remove(s)
                print('删除成功！')
                return
        print('学生信息不存在！')
    def query_student(self):
        name1 = input('请输入要打印成绩的学生姓名')
        for s in self.student_list:
            if s.name == name1:
                print(f'学生成绩为{s}')
                return
        print('学生信息不存在！')
    def show_student(self):
        for s in self.student_list:
            print(s)
    #运行教务系统的方法
    def run(self):
        print('欢迎使用教务系统！')
        while True:
            print('''
                    #########教务系统#########
                    #     1.添加学生信息      #
                    #     2.修改学生信息      #
                    #     3.删除学生信息      #
                    #     4.查询学生信息      #
                    #     5.列出所有学生      #
                    #     6.退出教务系统      #
                    #########################
            ''')
            choice=int(input('请输入要执行的操作:'))
            try:
                match choice:
                    case 1:
                        self.add_student()
                    case 2:
                        self.update_student()
                    case 3:
                        self.del_student()
                    case 4:
                        self.query_student()
                    case 5:
                        self.show_student()
                    case 6:
                        print('退出成功！')
                        break
                    case _:
                        print('输入不合法！')
            except Exception as e:
                print("出错了",e)


if __name__=='__main__':
    edu_management=EduManagement()
    edu_management.run()








