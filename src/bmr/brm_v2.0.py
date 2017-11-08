"""
    作者：彭鹏
    功能：BMR基础代谢率的计算
    版本： 2。0
    时间：08／11／2017
    新增功能：根据用户输入计算，持续输入
"""


def main():
    """
        祝函数
    """
    y_or_n = input('是否退出程序（y／n）')
    while y_or_n != 'y':
        # 性别
        gender = input('性别：')

        # 体重（kg）
        weight = float(input('体重（kg）：'))

        # 身高（cm）
        height = float(input('身高（cm）：'))

        # 年龄
        age = int(input('年龄：'))

        if gender == '男':
            # 男性bmr
            bmr = (13.7 * weight) + (0.5 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性bmr
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('基础代谢率（大卡）：', bmr)
        else:
            print('暂不支持')

        print()
        y_or_n = input('是否退出程序（y／n）')

if __name__ == '__main__':
    main()
