class Shape:
    def __init__(self, triangle, square):
        self.triangle_row = triangle
        self.square_row = square

    def triangle(self):
        if self.triangle_row != 5:
            print("Shape Not Required")
        else:
            for i in range(1, self.triangle_row + 1):
                rows = "* "
                print(" " * (self.triangle_row - i) + rows * (i))

    def square(self):
        if self.square_row != 5:
            print("Shape Not Required")
        else:
            for i in range(1, self.square_row + 1):
                rows = "*"
                print("*" * (self.square_row - i) + rows * (i))


test = Shape(5, 5)
test.triangle()
test.square()
