"""
    作者：彭鹏
    版本：2。0
    功能：AQI计算
    日期：10／11／2017
    2.0增加功能：AQI计算读取、写入json文件
"""
import json

def process_json_file(filepath):
    """
        解码json文件
    """
    f = open(filepath, mode='r', encoding='utf-8')
    city_list = json.load(f)
    return city_list


def main():
    """
        主函数
    """
    filepath = input('请输入json文件名称：')
    city_list = process_json_file(filepath)
    city_list.sort(key=lambda city: city['aqi'])
    top3_list = city_list[:3]

    f = open('top3_aqi.json', mode='w', encoding='utf-8')
    json.dump(top3_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()