"""
    作者：彭鹏
    版本：4。0
    功能：模拟投掷一个骰子
    日期：10／11／2017
    2.0 增加功能：模拟投掷2个骰子，并输出结果
    3.0 增加功能：可视化抛掷骰子结果(散点图)
    4.0 增加功能：对结果进行简单的数据统计和分析
"""
import random
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family']='sans-serif'
plt.rcParams['axes.unicode_minus'] = False


def roll_dice():
    """
        模拟掷骰子
    """
    roll = random.randint(1, 6)
    return roll

def main():
    """
        主函数
    """
    total_times = 10000

    #记录第一个骰子的结果
    roll_list = []

    for i in range(total_times):
        roll1 = roll_dice()
        roll2 = roll_dice()

        roll_list.append(roll1 + roll2)

    # 数据可视化
    plt.hist(roll_list, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    # print(plt.rcParamsDefault)
    plt.show()


if __name__ == '__main__':
    main()