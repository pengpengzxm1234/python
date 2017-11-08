"""
    作者：彭鹏
    功能：BMR基础代谢率的计算
    版本： 3。0
    时间：08／11／2017
    新增功能：用户可以在一行输入信息，带单位的信息输出
"""


def main():
    """
        祝函数
    """
    y_or_n = input('是否退出程序（y／n）')
    while y_or_n != 'y':
        print('请输入以下信息，用空客分割')
        input_str = input('性别 体重（kg）身高（cm）年龄：')
        str_list = input_str.split(' ')
        gender = str_list[0]
        weight = float(str_list[1])
        height = float(str_list[2])
        age = int(str_list[3])

        if gender == '男':
            # 男性bmr
            bmr = (13.7 * weight) + (0.5 * height) - (6.8 * age) + 66
        elif gender == '女':
            # 女性bmr
            bmr = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 655
        else:
            bmr = -1

        if bmr != -1:
            print('您的性别：{}， 体重：{}公斤，身高：{}厘米，年龄：{}岁'.format(gender, weight, height, age))
            print('基础代谢率：{}大卡'.format(bmr))
        else:
            print('暂不支持')

        print()
        y_or_n = input('是否退出程序（y／n）')

if __name__ == '__main__':
    main()
