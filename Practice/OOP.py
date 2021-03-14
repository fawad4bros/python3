# Practice #
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         print(name)
#     def add_one(self, x):
#         return x + 1
#     def bark(self):
#         print("Bark")
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_age(self,age):
#         self.age = age

#*******************************************************************************#

# Basic of CLASS and OBJECTS #
# class Student:
#     def __init__(self, name , age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade # 0 - 100
#     def get_grade(self):
#         return self.grade
# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
# s1 = Student("Jawad",35,95)
# s2 = Student("Saad",32,90)
# s3 = Student("Hammad",29,85)
# s4 = Student("Fawad",22,80)
# course = Course("Science", 3)
# course.add_student(s1)
# course.add_student(s2)
# course.add_student(s3)
# print(course.get_average_grade())

#*******************************************************************************#

# Inheritance #
# class Pet:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old")
#     def speak(self): #override this method
#         print("Dont know what to say")
# class Dog(Pet):
#     def speak(self): #If there is method defined in lower level class Or in the Child class that is the same name as the upper level class it will automatically override the upper method
#         print("Bark")
# class Cat(Pet):
#     def __init__(self, name, age, color):
#         super().__init__(name,age) # Super stand for the class from which we Inherit "PET". "__init__" is the method we want to call. "name","age" are the argument will be passed
#         self.color = color
#     def speak(self):
#         print("Mewo")
#     def show(self):
#         print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")
# class Fish(Pet):
#     pass
# p = Pet("Tim",19)
# p.show()
# p.speak()

# c = Cat("Tom",25,"Brown")
# c.show()
# c.speak()

# d = Dog("Tommy",5)
# d.show()
# d.speak()

# f = Fish("Bubbles", 10)
# f.speak()

#*******************************************************************************#

# Class method Class Attribute #

# class Person:
#     number_of_people = 0 #Class Attribute
#     GRAVITY = -9.8

#     def __init__(self, name):
#         self.name = name
#         Person.add_person()
#     @classmethod #Decorator
#     def number_of_people_(cls):
#         return cls.number_of_people
#     @classmethod
#     def add_person(cls):
#         cls.number_of_people += 1
# p1 = Person("Tim")
# p2 = Person("Jill")

# print(Person.number_of_people_())

#*******************************************************************************#

# Static Method # 

class Math:
    @staticmethod
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print("Run")

print(Math.add5(5))
print(Math.add10(10))
Math.pr()
