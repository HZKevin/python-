# class Point:
#     def __init__(self, x, y):
#         self.x =x
#         self.y =y
    
#     def __add__(self, other):
#         return Point(self.x + other.x,self.y +other.y)

# point = Point(10,20)
# other = Point(1,2)
# combined = point + other
# print(combined.x) 
#######container
# class TagCloud:
#     def __init__(self):
#         self.tags ={}
    
#     def add(self, tag):
#         self.tags[tag] =self.tags.get(tag, 0) + 1

# cloud =TagCloud()
# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# print(cloud.tags)


####properties
# class Product:
#     def __init__(self, price):
#         self.set_price(price)

#     def get_price(self):
#         return self.__price
    
#     def set_price(self, value):
#         if value < 0:
#             raise ValueError("invalid")
#         self.__price =value
#     price =property(get_price, set_price)

# product = Product(10)

# print(product.price)



 ##using decrator
# class Product:
    
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price
    
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("invalid")
#         self.__price =value
#     #当使用decrator时不需要单独声明
#     #price =property(get_price, set_price)

# product = Product(10)

# print(product.price)

##inheritance继承
# class Animal:
#     def __init__(self):
#         self.age = 1
#     def eat(self):
#         print("eat")
   
# class Mammal(Animal):
    
#     def walk(self):
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         print("swim")

# m=Mammal()
# m.eat()
# print(m.age)

# #objected class
# class Animal(object):
#     def __init__(self):
#         self.age = 1
#     def eat(self):
#         print("eat")
   
# class Mammal(Animal):
    
#     def walk(self):
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         print("swim")

# m=Mammal()
# print(isinstance(m, object))
# print(issubclass(Mammal,object))



#overriding
# class Animal(object):
#     def __init__(self):
#         print("animal construc")
#         self.age = 1
#     def eat(self):
#         print("eat")
#当不在同一层级时不能直接调用，需要用super   
# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("mamal consturctor")
#         self.weight = 2
#     def walk(self):
#         print("walk")

# class Fish(Animal):
#     def swim(self):
#         print("swim")

# m=Mammal()
# print(m.age)
# print(m.weight)


##muti inheritance
class Employee:
    def greet(self):
        print("emplyee greet")
        
  
class Person:
    def greet (self): 
        print("person greet")

class Mannager(Person,Employee):
    pass
manager = Mannager()
manager.greet()






