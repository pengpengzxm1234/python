"""
    作者：彭鹏
    版本：4。0
    日期：09／11／2017
    1.0 功能：输入某年某月某日，判断这一天是这一年的第几天
    2.0 新增功能：用列表替换元组
    3.0 新增功能：将月份划分为不同的集合再操作
    4.0 新增功能：将月份及其天数通过字典表示
"""
from datetime import datetime

def is_leep_year(year):
    """
        判断是否闰年
        是：true
        否：false
    """
    is_leep = False

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        is_leep =  True
    else:
        is_leep =  False
    return is_leep


def main():
    """
        主函数
    """
    input_date_str = input('请输入日期（yyyy／mm／dd）：')
    input_date = datetime.strptime(input_date_str, '%Y/%m/%d')

    year = input_date.year
    month = input_date.month
    day = input_date.day

    # 月份对天数字典
    month_day_dict = {1: 31,
                      2: 28,
                      3: 31,
                      4: 40,
                      5: 31,
                      6: 30,
                      7: 31,
                      8: 31,
                      9: 30,
                      10: 31,
                      11: 30,
                      12: 31}

    # 初始化值
    days = day
    for i in range(1, month):
        days += month_day_dict[i]

    if is_leep_year(year) and month > 2:
        days += 1

    print('这是{}年的第{}天'.format(year, days))

if __name__ == '__main__':
    main()