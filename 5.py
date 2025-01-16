class Cube:
    def __init__(self, edge):
        self.__edge = edge

    @property
    def edge(self):
        return self.__edge

    @edge.setter
    def edge(self, value):
        if value <= 0:
            raise ValueError("Edge length must be a positive number")
        self.__edge = value

    def display_volume(self):
        volume = self.__edge ** 3
        print(f"The volume of the cube is: {volume}")

    def display_one_surface(self):
        surface = self.__edge ** 2
        print(f"The surface area of one side of the cube is: {surface}")

    def display_total_surface(self):
        total_surface = 6 * (self.__edge ** 2)
        print(f"The total surface area of the cube is: {total_surface}")

def main():
    edge_length = float(input("Enter the edge length of the cube: "))
    cube = Cube(edge_length)
    cube.display_volume()
    cube.display_one_surface()
    cube.display_total_surface()

if __name__ == "__main__":
    main()