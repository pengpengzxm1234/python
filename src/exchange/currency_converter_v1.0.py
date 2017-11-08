"""
    功能：汇率兑换
    版本：1。0
"""

# 汇率 常量大写
USD_VS_RMB = 6.77

# 人名币输入
rmb_str_value = input('请输入人名币（CNY）金额：')

# 将字符串转换为数字
rmb_value = eval(rmb_str_value)

# 汇率计算
usd_value = rmb_value / USD_VS_RMB

# 输出结果
print('美元（USD）金额是：', usd_value)

