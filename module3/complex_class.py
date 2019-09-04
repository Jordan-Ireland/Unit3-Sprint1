class Complex:
    def __init__(self, real_number, imaginary_number):
        self.r = real_number
        self.i = imaginary_number

    def add(self, number):
        return self.r + number, self.i + number

    def subtract(self,number):
        return self.r - number, self.i - number

    def multiply(self,number):
        return self.r * number, self.i * number

    def divide(self,number):
        return self.r / number, self.i / number


x = Complex(3.0,-4.5)
print(x.r,x.i)
print(x.add(5))
print(x.subtract(5))
print(x.multiply(5))
print(x.divide(5))