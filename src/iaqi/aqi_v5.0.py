"""
    作者：彭鹏
    版本：5。0
    功能：AQI计算
    日期：13／11／2017
    2.0增加功能：AQI计算读取、写入json文件
    3.0增加功能：cvs
    4.0功能：判断文件格式，进行相应的操作
    5.0功能：通过爬虫获取实时数据
"""
import requests


def get_html_text(url):
    """
        返回url文本
    """
    r = requests.get(url, timeout=30)
    # print(r.status_code)
    return r.text


def main():
    """
        主函数
    """
    city_pinyin = input('请输入城市拼音：')
    url = 'http://pm25.in/' + city_pinyin
    url_text = get_html_text(url)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index + len(aqi_div)
    end_index = begin_index + 2
    aqi_value = url_text[begin_index: end_index]
    print('空气质量为：{}'.format(aqi_value))


if __name__ == '__main__':
    main()