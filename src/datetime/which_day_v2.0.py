"""
    作者：彭鹏
    版本：2。0
    日期：09／11／2017
    1.0 功能：输入某年某月某日，判断这一天是这一年的第几天
    2.0 新增功能：用列表替换元组
    总结：元组内容不可改变
         元组表示结构，列表表示顺序
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

    # 计算之前每月的天数综合以及当前月份的天数
    days_in_month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leep_year(year):
        days_in_month_list[1] = 29

    days = sum(days_in_month_list[: month -1]) + day

    print('这是{}年的第{}天'.format(year, days))

if __name__ == '__main__':
    main()