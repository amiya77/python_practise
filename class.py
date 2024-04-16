# class person:
#     name = "AM"
#     age = "30"
#     designation = "soldier"

#     def info(self):
#         print(f"{self.name} is a {self.designation}")

# a = person()
# # a.name = "mind"
# #a.occupation = "accountant"
# a.info()

#Class init method---------------------------------------

# class Snake:
#     def __init__(self, name):
#         self.name = name


# def change_name(self, new_name):
#     self.name = new_name

# python = Snake("Python")
# anaconda = Snake("Anaconda")

# print(python.name)
# print(anaconda.name)


#object method-------------------------------------------
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def my_func(self):
#         print("my name is " + self.name)
# p1 = Person("John", 36)
# p1.my_func()

#------------------------------------

# class Flat:
#     def __init__(self, name, colour):
#         self.name = name
#         self.colour = colour
#     def my_func(self):
#         print("my flat name is " + self.name + "." " it has " +  self.colour + ".")
# c1 = Flat("vrindavan", "safron")
# c1.my_func()
#-------------------------------------

#1 : static method-------------------------
# class Calculator:
#     def addNumbers(x, y):
#         return(x + y)
# Calculator.addNumbers = staticmethod(Calculator.addNumbers)
# print("total is", + Calculator.addNumbers(15,25))

#2
# class MyClass:
#     def __init__(self, value):
#         self.value = value

#     def get_max_value(x, y):  # Added staticmethod decorator
#         return max(x, y)

# print(MyClass.get_max_value(20, 30))  # Static method call


class MyClass:
    def __init__(self, value):
        self.value = value
    def get_max_value(x, y):
        return max(x, y)
print(MyClass.get_max_value(20, 50))

