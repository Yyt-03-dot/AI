print('''
#########教务系统#########
#     1.添加学生信息      #
#     2.修改学生信息      #
#     3.删除学生信息      #
#     4.查询学生信息      #
#     5.列出所有学生      #
#     6.统计班级成绩      #
#     7.退出教务系统      #
#########################
''')
all_stu={}
while True:
    choice=input('请输入要执行的操作')
    match choice:
        case '1':
            name1=input('请输入学生姓名')
            if name1 not in all_stu:
                chinese=float(input('请输入学生的语文成绩'))
                match = float(input('请输入学生的数学成绩'))
                english = float(input('请输入英语的语文成绩'))
                all_stu[name1]=(chinese,match,english)
                print('录入成功！')
                continue
            else:
                print('信息已存在！请重新录入！')
        case '2':
            name2 = input('请输入要修改的学生姓名')
            if name2 in all_stu:
                chinese2 = float(input('请输入学生的语文成绩'))
                match2 = float(input('请输入学生的数学成绩'))
                english2 = float(input('请输入英语的语文成绩'))
                all_stu[name2] = (chinese2, match2, english2)
                print('修改成功！')
            else:
                print('学生不存在！')
        case '3':
            name3 = input('请输入要删除的学生姓名')
            if name3 in all_stu:
                del all_stu[name3]
                print('删除成功！')
            else:
                print('学生不存在！')
        case '4':
            name4 = input('请输入要查询的学生姓名')
            if name4 in all_stu:
                a,b,c=all_stu[name4]
                print(f'学生{name4}的语文成绩为{a}，数学成绩为{b}，英语成绩为{c}')
            else:
                print('学生不存在！')
        case '5':
            if all_stu=={}:
                print('学生名单为空！')
            else:
                print('学生姓名\t\t语文成绩\t\t数学成绩\t\t英语成绩\t\t')
                for key,value in all_stu:
                    print(key,value[0],value[1],value[2])
        case '6':
            if all_stu == {}:
                print('学生名单为空！')
            else:
                max_ch_score=-1
                max_ch_name=''
                min_ch_score=101
                min_ch_name=''
                max_math_score = -1
                max_math_name = ''
                min_math_score = 101
                min_math_name = ''
                max_eng_score = -1
                max_eng_name = ''
                min_eng_score = 101
                min_eng_name = ''
                cn_sum_score=0
                math_sum_score = 0
                eng_sum_score = 0
                for key,value in all_stu.items() :
                    if value[0]>max_ch_score:
                        max_ch_score=value[0]
                        max_ch_name=key
                    if value[0]<min_ch_score:
                        min_ch_score=value[0]
                        min_ch_name=key
                    if value[1] > max_math_score:
                        max_math_score = value[1]
                        max_math_name = key
                    if value[1] < min_math_score:
                        min_math_score = value[1]
                        min_math_name = key
                    if value[2] > max_eng_score:
                        max_eng_score = value[2]
                        max_eng_name = key
                    if value[2] < min_eng_score:
                        min_eng_score = value[2]
                        min_eng_name = key
                    cn_sum_score +=value[0]
                    math_sum_score += value[1]
                    eng_sum_score += value[2]
                    avg_cn_score=(cn_sum_score/len(all_stu))
                    avg_math_score = (math_sum_score / len(all_stu))
                    avg_eng_score = (eng_sum_score / len(all_stu))
                    print(f'''
                            语文最高分姓名为{max_ch_name}分数为{max_ch_score},语文最低分姓名为{min_ch_name}分数为{min_ch_score}，语文平均分为{avg_cn_score}\t
                            数学最高分姓名为{max_math_name}分数为{max_math_score}，数学最低分姓名为{min_math_name}分数为{min_math_score}，数学平均分为{avg_math_score}\t
                            英语最高分姓名为{max_eng_name}分数为{max_eng_score}，英语最低分姓名为{min_eng_name}分数为{min_eng_score}，英语平均分为{avg_eng_score}\t
                            
                            ''' )
        case '7':
            print('退出成功！')
            break
        case _:
            print('输入无效！')

