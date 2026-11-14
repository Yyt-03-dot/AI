# match day:
#     case"1":
#         print()
#     case"2"|"3":
#         print()
#     case"4"|"5":
#         print()
#     case _
# #         print()
# #
#
# a=float(input('a'))
# b=float(input('b'))
# c=input('+ - * /')
# match c:
#
#     case "+" :
#         print('a+b=',a+b)
#     case "-":
#         print('a-b=',a-b)
#     case "*":
#         print('a*b=',a*b)
#     case"/" if b!=0 :
#         print('a/b=',a/b)
#     case _:
#         print('no')

a=input('zhiling')
match a:
    case"上"|"w"|"W":
        print('向上移动')
    case"下"|"s"|"S":
        print('向下移动')
    case"左"|"a""A":
        print('向左移动')
    case"右"|"d"|"D":
        print('向右移动')
    case"跳"|" ":
        print('跳跃')
    case"攻击"|"j"|"J":
        print('攻击')
    case"退出"|"esc"|"ESC":
        print('退出')
    case _:
        print('输入错误！')
