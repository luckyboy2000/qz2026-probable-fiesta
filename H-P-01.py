class Shape:

    '''def __init__(self, shape):
        self.shape = shape
        self.size = 0'''

    def area(self):
        return 0


class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):
        self.size = self.radius * self.radius * 3.14

        return self.size


class Square(Shape):

    def __init__(self, side):

        self.side = side

    def area(self):
        self.size = self.side * self.side

        return self.size


if __name__ == '__main__':
    # 初始化两个子类实例，存入列表
    shape_list = [Circle(4), Square(4)]
    # 遍历列表，统一调用area()方法，无需判断对象具体类型
    for shape in shape_list:
        print(shape.area())