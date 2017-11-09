"""
    作者：彭鹏
    功能：52周存钱挑战
    版本：4。0
    日期：09／11／2017
    2.0 新增功能：记录每周的存款数
    3.0 新增功能：使用循环直接计数
    4.0 新增功能：灵活设置每周的存款数，增加的存款数及存款周数
"""
import math

# 全局变量
saving = 0

def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
        计算n周内的存款金额
    """
    # global saving        # 声明使用全局变量
    money_list = []      # 记录每周存款数的列表

    for i in range(total_week):
        # 存钱操作
        # saving += money_per_week

        money_list.append(money_per_week)
        saving = math.fsum(money_list)

        # 输出信息
        # print('第{}周，存入{}元，账户累计{}元'.format(i + 1, money_per_week, saving))

        # 更新下周存入的金额
        money_per_week += increase_money

    return saving

def main():
    """
        主函数
    """
    money_per_week = float(input('请输入每周存入的金额：'))  # 每周存入的金额
    increase_money = float(input('请输入每周递增的金额：'))  # 递增的金额
    total_week = int(input('请输入总的周数：'))      # 总共的周数

    # 调用函数
    saving = save_money_in_n_weeks(money_per_week, increase_money, total_week)
    print('总存款金额', saving)

if __name__ == '__main__':
    main()
