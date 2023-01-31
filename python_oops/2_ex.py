class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"hi, I'm {self.name}")

person1 = Person("Sabya")
person1.talk()
person2 = Person("Kevin")
person2.talk()