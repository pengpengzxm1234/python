"""
    作者：彭鹏
    版本：9。0
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
"""
import pandas as pd



def main():
    """
        主函数
    """
    aqi_data = pd.read_csv('china_city_aqi.csv')
    print('基本信息：')
    print(aqi_data.info())

    print('数据预览：')
    print(aqi_data.head())

    # 基本统计
    print('AQI最大值：', aqi_data['AQI'].max())
    print('AQI最小值：', aqi_data['AQI'].min())
    print('AQI平均值：', aqi_data['AQI'].mean())

    # top10
    top10_citys = aqi_data.sort_values(by=['AQI']).head(10)
    print('空气质量最好的十个城市：')
    print(top10_citys)

    # bottom10
    # bottom10_citys = aqi_data.sort_values(by=['AQI']).tail(10)
    bottom10_citys = aqi_data.sort_values(by=['AQI'], ascending=False).head(10)
    print('空气质量最差的十个城市：')
    print(bottom10_citys)

    # 保存成csv
    top10_citys.to_csv('top10_aqi.csv', index=False)
    bottom10_citys.to_csv('bottom_aqi_csv', index=False)


if __name__ == '__main__':
    main()