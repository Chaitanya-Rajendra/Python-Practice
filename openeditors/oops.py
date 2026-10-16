# OOP = object Oriented Programming
# It is a Programming approach where we organize our proogram around objects 
# rather than only functions and variables

# Student:
# Data:
# - name, age, marks, roll_no
# Behaviour:
# - study(), attend_classes(), write_exam(), display_data

# in OOps, we combine data + behaviour into object

# 2. Class: Blueprint/Template to create objects(no memory allocation)

# 3. Object: Instances of class, Actual thing created from blueprint(contains memory allocation)

# class Student:
#   pass
# student1 = Student() #student1 -> object
# student2 = Student() 

# Attributess- are the data/properties associated with a object.

# class Student:
#   pass
# student1 = Student()
# student1.name = "Rahul"
# student1.age = 23
# student1.marks = 95
# print(student1.name)
# print(student1.age)
# print(student1.marks)

# Methods - Functions created inside class

# class Student:
#   def study(self):
#     print("Student is studying")
# student1 = Student()
# student1.study()
# Method only belongs to class

# Constructor- It is a special method that is automatically called when an object is created.

# __init__() 

# class Student:
#   def __init__(self):
#     print("Student is studying")
# student1 = Student()

# Constructor with attributes

# class Student:
#   def __init__(self, name, age, marks):
#     self.name = name
#     self.age = age
#     self.marks = marks
# student1 = Student("Chaitu", 22, 90)
# print(student1.name)
# print(student1.age)
# print(student1.marks)
# Self represents current object.

# class Student:
#   def __init__(self, name, age, marks):
#     self.name = name
#     self.age = age
#     self.marks = marks
#   def display(self):
#     print(self.name, self.age, self.marks)
# student1 = Student("Chaitu", 22, 90)
# student1.display()

# Encapsulation()- Bundling data and methods together inside a class and 
# controlling how that data is accessed or modified.

# class BankAccount:
#   def __init__(self, balance):
#     self._balance = balance
#   def deposit(self, amount):
#     if amount > 0:
#       self._balance +=  amount
#   def withdraw(self, amount):
#     self._balance -= amount
#   def get_balance(self):
#     return self._balance
# balance = BankAccount(50000)
# balance.deposit(10000)
# balance.withdraw(5000)
# print(balance.get_balance())

# Double underscore indicates a private like attribute in python through name managing

# Getter and Setter Concept

# Private DeprecationWarning
# Getter -> Read Data
# Setter -> Modify data safely

# class Student:
#   def __init__(self, marks):
#     self._marks = marks
#   def get_marks(self):
#     return self._marks
#   def set_marks(self, marks):
#     if 0 <= marks <= 100:
#       self._marks = marks
#     else:
#       print("InValid marks")
# student = Student(80)
# print(student.get_marks())
# student.set_marks(90)
# print(student.get_marks())


# Inheritance- Process of acquring properties from parent to child class. 
# It allows us to create a new class based on an existing class, inheriting its 
# attributes and methods.

# Types of Inheritance:
# 1. Single Inheritance- one parent class and one child class
#Parent class
# class Animal:
#   def speak(self):
#     print("Animal speaks")
# #Child Class
# class Dog(Animal):
#   def bark(self):
#     print("Dog barks")
# l = Dog()
# l.speak()
# l.bark()

# 2. Multiple Inheritance- one child class and multiple parent classes
# class Father:
#   def father_properties(self):
#     print("Father's property")
# class Mother:
#   def mother_properties(self):
#     print("Mother's property")
# #Child class
# class Child(Father, Mother):
#   def child_properties(self):
#     print("Child's property")
# c = Child()
# c.father_properties()
# c.mother_properties()
# c.child_properties()

# 3. Multilevel Inheritance- one parent class, one child class and one grandchild class
#GrandParent -> Parent -> Child
# class GrandParent:
#   def house(self):
#     print("Grandparent's house")
# class Parent(GrandParent):
#   def car(self):
#     print("Parent's car")
# class Child(Parent):
#   def bike(self):
#     print("Child's bike")
# c = Child()
# c.house()
# c.car()
# c.bike()

# 4. Hierarchical Inheritance- one parent class and multiple child classes
# class Animal:
#   def eat(self):
#     print("Animal eats")
# #Child class 1
# class Dog(Animal):
#   def bark(self):
#     print("Dog barks")
# #Child class 2
# class Cat(Animal):
#   def meow(self):
#     print("Cat meows")
# d = Dog()
# c = Cat()
# d.eat()
# d.bark()
# c.eat()
# c.meow()

# 5. Hybrid Inheritance- combination of multiple and multilevel inheritance
# class A:
#   def method_a(self):
#     print("A")
# class B(A):
#   def method_b(self):
#     print("B")
# class C(A):
#   def method_c(self):
#     print("C")
# class D(B, C):
#   def method_d(self):
#     print("D")
# obj = D()
# obj.method_a()
# obj.method_b()
# obj.method_c()
# obj.method_d()

# Super method- In python super() is used to access functionality from the parent class

# class Parent:
#   def show(self):
#     print("Parent method")
# class Child(Parent):
#   def show(self):
#     super().show() #Accessing parent method
#     print("Child method")
# c = Child()
# c.show()

#super() with constructor
# class Person:
#   def __init__(self, name):
#     self.name = name
# class Student(Person):
#   def __init__(self, name, marks):
#     super().__init__(name)
#     self.marks = marks
# s = Student("Chaitu", 90)
# print(s.name)
# print(s.marks)


# Vehicle and Car
# Vehicle -> Car
# Vehicle - start(), stop()
# Car - drive


# class Vehicle:
#   def start(self):
#     print("Vehicle started")
#   def stop(self):
#     print("Vehicle stopped")
# class Car(Vehicle):
#   def drive(self):
#     print("Car is driving")
# v = Vehicle()
# c = Car()
# c.start()
# c.drive()
# c.stop()


#Person and Student
# Person -> Student
# Person - name, age, display_person()
# Student - roll_no, course, display_student()
# Output:
# Name, age, roll_no, course

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def display_person(self):
#     print("Name:", self.name)
#     print("Age:", self.age)
# class Student(Person):
#   def __init__(self, name, age, roll_no, course):
#     super().__init__(name, age)
#     self.roll_no = roll_no
#     self.course = course
#   def display_student(self):
#     self.display_person()
#     print("Roll No:", self.roll_no)
#     print("Course:", self.course)

# s = Student("Chaitu", 20, 123, "Computer Science")
# s.display_student()