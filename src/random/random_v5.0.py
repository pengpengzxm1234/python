"""
    作者：彭鹏
    版本：5。0
    功能：模拟投掷一个骰子
    日期：10／11／2017
    2.0 增加功能：模拟投掷2个骰子，并输出结果
    3.0 增加功能：可视化抛掷骰子结果(散点图)
    4.0 增加功能：对结果进行简单的数据统计和分析
    5.0 增加功能：使用科学计算库简化程序，完善数据可视化结果
"""
import matplotlib.pyplot as plt
import numpy as np




def main():
    """
        主函数
    """
    total_times = 10000

    # 记录第一个骰子的结果
    roll1_arr = np.random.randint(1, 7, size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr

    hist, bins = np.histogram(result_arr, bins=range(2, 14))
    print(hist)
    print(bins)

    # 数据可视化
    plt.hist(result_arr, bins=range(2, 14), normed=1, edgecolor='black', linewidth=1, rwidth=0.8)

    #设置x轴坐标点
    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点',
                   '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos, tick_labels)
    plt.title('骰子点数统计')
    plt.xlabel('点数')
    plt.ylabel('频率')
    # print(plt.rcParamsDefault)
    plt.show()


if __name__ == '__main__':
    main()