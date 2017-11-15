"""
    作者：彭鹏
    版本：10。0
    功能：AQI计算
    日期：13／11／2017
    2.0增加功能：AQI计算读取、写入json文件
    3.0增加功能：cvs
    4.0功能：判断文件格式，进行相应的操作
    5.0功能：通过爬虫获取实时数据
    6.0功能：通过爬虫获取实时数据，使用beautifulSoup解析网页
    7.0功能：通过爬虫获取实时数据，使用beautifulSoup解析网页,获取所有城市的aqi
    8.0功能：通过爬虫获取实时数据，使用beautifulSoup解析网页,获取所有城市的aqi,并保存到scv文件中
    9.0功能：分析数据 pandas
    10.0功能：数据清洗，利用pandas进行数据可视化
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 数据清洗
    # 只保留AQI大于0的数据
    # filter_condition = aqi_data['AQI'] > 0
    # clean_aqi_data = aqi_data[filter_condition]

    clean_aqi_data = aqi_data[aqi_data['AQI'] > 0]

    # 基本统计
    print('AQI最大值：', clean_aqi_data['AQI'].max())
    print('AQI最小值：', clean_aqi_data['AQI'].min())
    print('AQI平均值：', clean_aqi_data['AQI'].mean())

    # top50
    top50_citys = clean_aqi_data.sort_values(by=['AQI']).head(50)
    top50_citys.plot(kind='bar', x='City', y='AQI', title='空气质量最好的50个城市',
                     figsize=(20, 10))
    plt.savefig('top50_aqi_bar.png')
    plt.show()


if __name__ == '__main__':
    main()
