"""
    作者：彭鹏
    功能：BMR基础代谢率的计算
    版本： 1。0
    时间：08／11／2017
"""


def main():
    """
        祝函数
    """

    # 性别
    gender = '男'

    # 体重（kg）
    weight = 70

    # 身高（cm）
    height = 175

    # 年龄
    age = 25

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

if __name__ == '__main__':
    main()
