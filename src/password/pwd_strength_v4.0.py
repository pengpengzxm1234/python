"""
    作者：彭鹏
    版本：4。0
    功能：判断密码强度
    日期：10／11／2017
    2.0 增加功能：限制密码设置次数；循环的终止
    3.0 增加功能：保存设置的密码及其对应强度到到文件中
    4.0 增加功能：读取保存的密码
"""


def check_number_exist(password_str):
    """
        判断字符中是否含有数字
    """
    has_number = False

    for c in password_str:
        if c.isnumeric():
            has_number = True
            break
    return has_number


def check_letter_exist(password_str):
    """
        判断字符中是否含有字母
    """
    has_letter = False

    for c in password_str:
        if c.isalpha():
            has_letter = True
            break
    return has_letter


def main():
    """
        主函数
    """

    f = open('password_v3.0.txt','r')

    # 1read() 读取全部
    # content = f.read()
    # print(content)

    # 2.readline() 读取一行
    # line = f.readline()
    # print(line)
    # line = f.readline()
    # print(line)

    # 3.readlines() 内容返回为列表形式
    #for line in f.readlines():
    for line in f:
        print('read:{}'.format(line))

    f.close()

if __name__ == '__main__':
    main()
