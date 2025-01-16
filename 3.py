class Pet:
    def __init__(self, kind, legs_number):
        self.__kind = kind
        self.__legs_number = legs_number

    @property
    def kind(self):
        return self.__kind

    @kind.setter
    def kind(self, value):
        if not value:
            raise ValueError("Kind cannot be empty")
        self.__kind = value

    @property
    def legs_number(self):
        return self.__legs_number

    @legs_number.setter
    def legs_number(self, value):
        if value < 0:
            raise ValueError("Legs number cannot be negative")
        self.__legs_number = value

    def start_running(self):
        print(f"{self.kind} is running")

    def stop_running(self):
        print(f"{self.kind} stopped")


dog = Pet("dog", 4)
dog.start_running()
dog.stop_running()

try:
    dog.kind = ""
except ValueError as e:
    print(e)

try:
    dog.legs_number = -1
except ValueError as e:
    print(e)