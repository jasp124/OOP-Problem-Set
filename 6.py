def display_menu():
    print("1. Enter radius")
    print("2. Display radius")
    print("3. Display diameter")
    print("4. Display area")
    print("5. Display perimeter")
    print("6. Exit")

class Circle:
    def __init__(self):
        self.__radius = None

    @property
    def radius(self):
        if self.__radius is None:
            raise ValueError("Radius has not been set")
        return self.__radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius cannot be negative or zero")
        self.__radius = value

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

def main():
    circle = Circle()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            try:
                radius = float(input("Enter the radius: "))
                circle.radius = radius
            except ValueError as e:
                print(e)
        elif choice == "2":
            try:
                print("Radius:", circle.radius)
            except ValueError as e:
                print(e)
        elif choice == "3":
            try:
                print("Diameter:", circle.get_diameter())
            except ValueError as e:
                print(e)
        elif choice == "4":
            try:
                print("Area:", circle.get_area())
            except ValueError as e:
                print(e)
        elif choice == "5":
            try:
                print("Perimeter:", circle.get_perimeter())
            except ValueError as e:
                print(e)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
