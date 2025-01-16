class Trigonometry:
    def square_area(self, side):
        return side ** 2

    def rectangle_area(self, base, height):
        return base * height

    def triangle_area(self, base, height):
        return (base * height) / 2

def main():
    trigonometry = Trigonometry()

    side = float(input("Enter the side of a square: "))
    print("The area of the square is:", trigonometry.square_area(side))

    base = float(input("Enter the base of a rectangle: "))
    height = float(input("Enter the height of a rectangle: "))
    print("The area of the rectangle is:", trigonometry.rectangle_area(base, height))

    base = float(input("Enter the base of a triangle: "))
    height = float(input("Enter the height of a triangle: "))
    print("The area of the triangle is:", trigonometry.triangle_area(base, height))

if __name__ == "__main__":
    main()