# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f"{self.name} says:woof!")

# #creating an instance of the dog class
# my_dog = Dog("buddy", 3)

# #accessing of attributes & calling methods of instance
# print(my_dog.name)
# print(my_dog.age)
# my_dog.bark()
#---------------------
#In method----------

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def bark(self):
        print(f"{self.get_name()} says woof , i am {self.get_age()} years old ")
my_dog = Dog("buddy", 3)
my_dog.bark()


