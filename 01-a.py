# print("Hello "*2)

# x = "False"
# print(bool(x))

# temperature_india = 5

# if temperature_india > 10:
#     print("Its high")
# print("done")

# message = "its hot" if temperature_india > 20 else "its cool"

# print(message)

# for i in range(5):
#     print("Hello", i)

# count = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         count += 1
#         print(i)

# print(f"We have {count} even numbers")

# coordinates = (1, 2, 5)
# x, y, z = coordinates

# print(x)

# try:
#     age = int(input("Age : "))
#     print(age)
# except ValueError:
#     print("Invalid type")

# class Point:
#     def move(self):
#         print("move")


# point1 = Point()
# point1.move()
# point1.x = 10
# print(point1.x)


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def talk(self):
#         print(f"Hello there, am {self.name}")


# p1 = Person("Noufan")
# p1.talk()


import random


class Dice:
    def roll(self):
        print(random.randint(1, 6))


d = Dice()
d.roll()
