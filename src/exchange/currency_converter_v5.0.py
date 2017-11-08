"""
    功能：汇率兑换
    版本：4。0
    2。0 新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
    3。0 新增功能：程序可以一直运行，直到用户退出
    4。0 新增功能：将汇率兑换功能封装到函数中
    5。0 新增功能：(1)使程序结构化 (2)简单函数定义 lambda
"""


# def convert_currency(im, er):
#     """
#         汇率兑换函数
#     """
#     out = im * er
#     return out

def main():
    """
        主函数
    """
    # 汇率 常量大写
    USD_VS_RMB = 6.77

    # 带单位的输入
    currency_str_value = input('请输入带单位的货币金额：')


    # 获取货币单位
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / USD_VS_RMB

    elif unit == 'USD':
        exchange_rate = USD_VS_RMB

    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        # 使用lamdba定义函数
        convert_currency2 = lambda x: x * exchange_rate

        # # 调用函数
        # out_money = convert_currency(in_money, exchange_rate)

        # 调用lamdba函数
        out_money = convert_currency2(in_money)
        print('转换后的金额：', out_money)

    else:
        print('不支持该货币')


if __name__ == '__main__':
    main()
