class Patient():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display(self):
        print(self.first_name)
        print(self.last_name)
        print(self.age)

    def say_if_minor(self):
        if (self.age < 21):
            print(self.first_name + " " + self.last_name + "  is a minor")

    def change_last_name(self, new_last_name):
        self.last_name = new_last_name
        print("New name is: " + self.first_name + " " + self.last_name)


patient1 = Patient("MT", "KK", 20)

patient1.display()

patient1.say_if_minor()

patient1.change_last_name("Dumbo")