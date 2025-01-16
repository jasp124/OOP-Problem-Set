class Pet:
    def __init__(self, kind, legs_number):
        self.kind = kind
        self.legs_number = legs_number

    def start_running(self):
        print(f"{self.kind} is running")

    def stop_running(self):
        print(f"{self.kind} stopped")

dog = Pet("Dog", 4)
monkey = Pet("Monkey", 4)

dog.start_running()
dog.stop_running()

monkey.start_running()
monkey.stop_running()