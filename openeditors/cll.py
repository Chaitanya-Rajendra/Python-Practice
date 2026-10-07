# class dog:
#     def sound(self):
#         print('dogs are barking')
# class cat:
#     def sound(self):
#         print('cats are the meows')
# d=dog()
# c=cat()
# d.sound()
# c.sound()

#   types of poly morphism
# ===========================
# 1) method overloading
# 2) method overriding
# 3)operator overloading



#    1) method overriding
# ==========================
# --- it occurs when a child class provide it's own implementation of a method  
# that alreaddy existing in a parent class


# class classroom:
#     def __init__(self,name,age,):
#         self.name=name
#         self.age=age
#     def display(self):
#         print(self.name,self.age)
# class students(classroom):
#     def __init__(self, name,age,rollno,course):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.course=course
#     def display(self):
#         super().display()
#         print(self.rollno,self.course)
# obj=students('rahul',25,67,'btech')
# obj.display()

# class Animal:
#     def sound(self):
#         print('Animal makes sound')
# class dog(Animal):
#     def sound(self):
#         print('dogs are barking')
# class cat(Animal):
#     def sound(self):
#         print('cats are the meows')
# d=dog()
# c=cat()
# d.so()
# d.sound()
# c.sound()


##   method overloading
# ==========================
#  --- having multiple methods with same name but different parameters

# class cal:
#     def add(self,a,b):
#         return a+b
#     def add(self,a,b,c):
#         return a+b+c
# call=cal()
# call.add(10,20)
# call.add(10,30,40)


# 1) default arguments
# ===========================


# class cal:
#     def add(self,a,b,c=0):
#         return a+b+c
# call=cal()
# print(call.add(10,20))
# print(call.add(10,30,40))



#    2)using  * args
# =========================                       

# class caluclator:
#     def add(self,*args):
#         return sum(args)
# cal=caluclator()
# print(cal.add(34,56,7,5,3))
# print(cal.add(45,34))



# 3) operator overloading
# =============================
# -- operator overloading means giving operators


# class point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __add__(self, other):
#         return  point(
#             self.x+other.x,
#             self.y+other.y
#         )
# p1=point(10,20)
# p2=point(30,50)
# p3=p1+p2
# print(p3.x)
# print(p3.y)


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def __eq__(self, other):
#         return self.marks==other.marks
# s1=student("a",56)
# s2=student('b',56)
# print(s1==s2)
        
        
#### abstraction
#============================
# --- it  means hiding unneccessary implementation details and 
# explosing only the required functionality


# from abc import ABC,abstractmethod
# class Animal(ABC):
#     @abstractmethod 
#     def sound(self):
#         pass
# class dog(Animal):
#     def sound(self):
#         print('dog barks')
# class cat(Animal):
#     def sound(self):
#         print('cat meows')
# d=dog()
# c=cat()
# d.sound()
# c.sound()
# animal=Animal()


# from  abc import ABC ,abstractmethod
# class payment(ABC):
#     @abstractmethod
#     def pay (self,amount):
#         pass
# class upi(payment):
#     def pay(self,amount):
#         print("paid",amount,'using upi')
# class credit(payment):
#     def pay(self,amount):
#         print('paid',amount,'usinng with  credit')
# up=upi()
# card=credit()
# up.pay(5000)
# card.pay(1000)