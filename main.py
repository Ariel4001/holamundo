class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    persona1=Person("John", 20)
    print(persona1.__dict__)