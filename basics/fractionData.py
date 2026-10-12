class Fraction:
    def __init__(self, x, y):
        self.num = x
        self.den = y

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den

        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den

        return "{}/{}".format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den

        return "{}/{}".format(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num

        return "{}/{}".format(new_num, new_den)


class main:
    obj = Fraction(2, 3)
    obj2 = Fraction(3, 5)
    obj3 = Fraction(5, 3)

    print(obj + obj2 + obj3)