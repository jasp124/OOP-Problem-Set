class Box:
    def __init__(self, width, length, height):
        self.__width = width
        self.__length = length
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive value")
        self.__width = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value <= 0:
            raise ValueError("Length must be a positive value")
        self.__length = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive value")
        self.__height = value

    def display_volume(self):
        volume = self.width * self.length * self.height
        print(f"The volume of the box is: {volume}")

    def display_dimensions(self):
        print(f"The dimensions of the box are: width = {self.width}, length = {self.length}, height = {self.height}")


def main():
    boxes = []
    for i in range(3):
        width = float(input(f"Enter the width of box {i+1}: "))
        length = float(input(f"Enter the length of box {i+1}: "))
        height = float(input(f"Enter the height of box {i+1}: "))
        box = Box(width, length, height)
        boxes.append(box)

    for i, box in enumerate(boxes):
        print(f"Box {i+1}:")
        box.display_dimensions()
        box.display_volume()
        print()


if __name__ == "__main__":
    main()