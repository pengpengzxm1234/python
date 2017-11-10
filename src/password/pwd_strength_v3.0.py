"""
    作者：彭鹏
    版本：3。0
    功能：判断密码强度
    日期：10／11／2017
    2.0 增加功能：限制密码设置次数；循环的终止
    3.0 增加功能：保存设置的密码及其对应强度到到文件中
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
    try_times = 5

    while try_times > 0:

        password = input('请输入密码：')

        # 密码强度
        strength_level = 0

        # 规则1：密码长度大于8
        if len(password) > 8:
            strength_level += 1
        else:
            print('密码长度不小于8位！')

        # 规则2：包含数字
        if check_number_exist(password):
            strength_level += 1
        else:
            print('密码要包含数字！')

        # 规则3：包含字母
        if check_letter_exist(password):
            strength_level += 1
        else:
            print('密码要包含字母！')

        stenngth_value = '弱'
        if strength_level == 3:
            stenngth_value = '强'
        elif strength_level == 2:
            stenngth_value = '中'

        f = open('password_v3.0.txt', 'a', encoding='utf8')  # 文件地址默认当前目录
        f.write('密码：{}，强度：{}\n'.format(password, stenngth_value))
        f.close()

        if strength_level == 3:
            print('恭喜！密码强度合格')
            break
        else:
            print("密码强度不合格")
            try_times -= 1

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')


if __name__ == '__main__':
    main()
