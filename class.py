# class person:
#     name = "harry"
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


#object class-------------------------------------------
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def my_func(self):
        print("my name is " + self.name)
p1 = Person("John", 36)
p1.my_func()
