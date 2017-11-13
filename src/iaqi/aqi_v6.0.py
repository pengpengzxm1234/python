"""
    作者：彭鹏
    版本：6。0
    功能：AQI计算
    日期：13／11／2017
    2.0增加功能：AQI计算读取、写入json文件
    3.0增加功能：cvs
    4.0功能：判断文件格式，进行相应的操作
    5.0功能：通过爬虫获取实时数据
    6.0功能：通过爬虫获取实时数据，使用beautifulSoup解析网页
"""
import requests
from bs4 import BeautifulSoup


def get_city_aqi(city_pinyin):
    """
        获取城市的aqi值
    """
    url = 'http://pm25.in/' + city_pinyin
    r = requests.get(url, timeout=30)
    soup = BeautifulSoup(r.text, 'lxml')
    div_list = soup.find_all('div', {'class': 'span1'})

    city_aqi = []
    for i in range(8):
        div_content = div_list[i]
        caption = div_content.find('div', {'class': 'caption'}).text.strip()
        value = div_content.find('div', {'class': 'value'}).text.strip()

        city_aqi.append((caption, value))
    return city_aqi


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    city_aqi = get_city_aqi(city_pinyin)

    print(city_aqi)


if __name__ == '__main__':
    main()