"""
    作者：彭鹏
    版本：6。0
    功能：判断密码强度
    日期：10／11／2017
    2.0 增加功能：限制密码设置次数；循环的终止
    3.0 增加功能：保存设置的密码及其对应强度到到文件中
    4.0 增加功能：读取保存的密码
    5.0 增加功能：相关方法封装成一个整体：面向对象编程，定义一个password工具类
    6.0 增加功能：将文件操作封装到一个类中
"""


class PasswordTool:
    """
        密码工具类
    """
    def __init__(self, password):
        # 类的属性
        self.password = password
        self.strength_level = 0

    # 类的方法
    def check_number_exist(self):
        """
            判断字符中是否含有数字
        """
        has_number = False

        for c in self.password:
            if c.isnumeric():
                has_number = True
                break
        return has_number

    def check_letter_exist(self):
        """
            判断字符中是否含有字母
        """
        has_letter = False

        for c in self.password:
            if c.isalpha():
                has_letter = True
                break
        return has_letter

    def process_password(self):
        # 规则1：密码长度大于8
        if len(self.password) > 8:
            self.strength_level += 1
        else:
            print('密码长度不小于8位！')

        # 规则2：包含数字
        if self.check_number_exist():
            self.strength_level += 1
        else:
            print('密码要包含数字！')

        # 规则3：包含字母
        if self.check_letter_exist():
            self.strength_level += 1
        else:
            print('密码要包含字母！')


class FileTool:
    """
        文件工具类
    """
    def __init__(self, filepath):
        self.filepath = filepath

    def write_to_file(self, line):
        f = open(self.filepath, 'a', encoding='utf8')
        f.write(line)
        f.close()

    def read_from_file(self):
        f = open(self.filepath,'r')
        lines = f.readlines()
        f.close()
        return lines


def main():
    """
        主函数
    """

    try_times = 5
    filepath = 'password_v6.0.txt'

    # 实例化文件工具类对象
    file_tool = FileTool(filepath)

    while try_times > 0:

        password = input('请输入密码：')

        # 实例话密码工具对象
        password_tool = PasswordTool(password)
        password_tool.process_password()

        # 写文件
        file_tool.write_to_file('密码：{}，强度：{}\n'.format(password, password_tool.strength_level))

        if password_tool.strength_level == 3:
            print('恭喜！密码强度合格')
            break
        else:
            print("密码强度不合格")
            try_times -= 1

        print()

    if try_times <= 0:
        print('尝试次数过多，密码设置失败！')

    # 读操作
    lines =  file_tool.read_from_file()
    print(lines)

if __name__ == '__main__':
    main()
