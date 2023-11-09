#Студет Степан
class Student:
    def __init__(self, name, age, sr):
        self.name = name
        self.age = age
        self.sr = sr


    def get_name(self):
        return self.name


    def set_name(self, name):
        self.name = name


    def get_age(self):
        return self.age


    def set_age(self, age):
        self.age = age


    def get_sr(self):
        return self.sr


    def set_gpa(self, sr):
        self.sr = sr
student1 = Student('Степааааааааааааааааааааааааааааан', 19, 2.9)


print("Имя студента:", student1.get_name())
print("Возраст студента:", student1.get_age())
print("Средний балл студента:", student1.get_sr())


student1.set_name("Zтепан")
student1.set_gpa(2.69)


print("Измененное имя студента:", student1.get_name())
print("Измененный средний балл студента:", student1.get_sr())






#ААА я Прямоугольник
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def get_area(self):
        return self.length * self.width



    def get_perimeter(self):
        return 2 * (self.length + self.width)


rectangle1 = Rectangle(100, 69)

area = rectangle1.get_area()
perimeter = rectangle1.get_perimeter()

print(f"Площадь прямоугольника: {area}")
print(f"Периметр прямоугольника: {perimeter}")





#Бибика
class Car:
    def __init__(self, make, model, yearoi, mileage):
        self.make = make
        self.model = model
        self.yearoi = yearoi
        self.mileage = mileage


    def set_make(self, make):
        self.make = make


    def set_model(self, model):
        self.model = model


    def set_yearoi(self, yearoi):
        self.yearoi = yearoi


    def set_mileage(self, mileage):
        self.mileage = mileage


    def get_make(self):
        return self.make


    def get_model(self):
        return self.model


    def get_yearoi(self):
        return self.yearoi


    def get_mileage(self):
        return self.mileage


    def dinfo(self):
        print(f"Марка: {self.make}")
        print(f"Модель: {self.model}")
        print(f"Год выпуска: {self.yearoi}")
        print(f"Пробег: {self.mileage} км")

car1 = Car("Chevrolet", "Corvette", 2024, 0)

car1.dinfo()

car1.set_make("Matiz")
car1.set_model("PLOv")
car1.set_mileage(900009)

car1.dinfo()





#БАнк
class BankAccount:
    def __init__(self, clname, initial_balance=0):
        self.clname = clname
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Внесена сумма {amount} руб. выполнен. Новый баланс: {self.balance} руб.")
        else:
            print("Вы выбрали не ту операцию")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Снятие на сумму {amount} руб. выполнено. Новый баланс: {self.balance} руб.")
        elif amount > self.balance:
            print("Недостаточно средств на счете.")


    def get_balance(self):
        print(f"Баланс {self.clname}: {self.balance} руб.")


account1 = BankAccount("Степан Козлов", 10000)

account1.deposit(556753)
account1.withdraw(69)

account1.get_balance()


#ХАХАХА Треугольный треугольник


import math
class Triangle:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def area(self):
        s = (self.x + self.y + self.z) / 2
        return math.sqrt(s * (s - self.x) * (s - self.y) * (s - self.z))

    def triangle_type(self):
        def is_equilateral():
            return self.x == self.y == self.z

        def is_isosceles():
            return self.x == self.y or self.y == self.z or self.z == self.x

        def is_scalene():
            return not is_equilateral() and not is_isosceles()

        if is_equilateral():
            return "Равносторонний треугольник"
        elif is_isosceles():
            return "Равнобедренный треугольник"
        elif is_scalene():
            return "Разносторонний треугольник"
        else:
            return "Неопределенный треугольник"

triangle1 = Triangle(4, 14, 14)
triangle2 = Triangle(10, 2, 6)
triangle3 = Triangle(9, 9, 9)

print(triangle1.triangle_type())
print(triangle2.triangle_type())
print(triangle3.triangle_type())

print("Площадь треугольника ", triangle3.area())