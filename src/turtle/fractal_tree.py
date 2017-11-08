"""
    作者：彭鹏
    功能：利用递归绘制分形树
    版本：1。0
    日期：08／11／2017
"""
import turtle


def draw_branch(branch_length):
    """
        绘制分形树
    """

    if branch_length < 35:
        # 变换颜色
        turtle.color('green')
    else:
        turtle.color('brown')

    if branch_length > 5:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length - 15)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 15)

        # 返回之前的树枝路径
        turtle.right(20)
        turtle.penup()
        turtle.backward(branch_length)
        turtle.pendown()

def main():
    """
        主函数
    """
    turtle.left(90)
    turtle.penup()
    turtle.backward(150)
    turtle.pendown()
    turtle.pensize(2)
    draw_branch(120)
    turtle.exitonclick()

if __name__ == '__main__':
    main()
