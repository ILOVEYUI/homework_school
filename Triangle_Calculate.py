class Triangle():
    """计算三角形面积和周长"""

    def __init__(self, a, b, c):
        """初始化边长abc"""
        self.a = a
        self.b = b
        self.c = c

    def jm(self):
        """判断三边是否能组成三角形"""
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return 1
        else:
            print("perimeter=0.0\narea=0.0\na=0.0,b=0.0,c=0.0")

    def perimeter(self):
        """计算三角形周长"""
        s = self.a + self.b + self.c
        print("perimeter=" + str(s))

    def calculate(self, si):
        """计算三角形面积"""
        Area = (si * (si - self.a) * (si - self.b) * (si - self.c)) ** 0.5
        print("area=" + str(Area))


a = float(input())
b = float(input())
c = float(input())
sigema = Triangle(a, b, c)
if sigema.jm():
    sigema.perimeter()
    sigema.calculate((a + b + c) / 2)
    print("a=" + str(a) + "," + "b=" + str(b) + "," + "c=" + str(c))
# ????
