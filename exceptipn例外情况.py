# try:
#     age = int(input("age= "))
#     xfactor = 10/age
# # except ValueError as ex:
# except ValueError:
#     print("invalid input")
#     # print(ex)
#     # print(type(ex))
# except ZeroDivisionError:
#     print("input cant be zero")
# else:
#     print("no exception thrown")
# print("continues")

# try:
#     age = int(input("age= "))
#     xfactor = 10/age
# except ValueError as ex:
#     print("invalid input")
#     print(ex)
#     print(type(ex))
# else:
#     print("no exception thrown")
# print("continues")

# try:
#     file = open("exceptipn例外情况.py")
#     age = int(input("age= "))
#     xfactor = 10/age
# except (ValueError,ZeroDivisionError):
#     print("input cant be zero")
#     file.close
# else:
#     print("no exception thrown")
# finally:
#     file.close
####using with statement
# try:
#     with open("exceptipn例外情况.py") as file:
#         print("file opened")
#         file.__exit__
#     age = int(input("age= "))
#     xfactor = 10/age
# except (ValueError,ZeroDivisionError):
#     print("input cant be zero")
# else:
#     print("stop")

# try:
#     with open("exceptipn例外情况.py") as file, open("another.text") as target:
#         print("file opened")
        
#     age = int(input("age= "))
#     xfactor = 10/age
# except (ValueError,ZeroDivisionError):
#     print("input cant be zero")
# else:
#     print("stop")

######cost of Raising exception
from timeit import timeit
def caculate_xfactor(age):
    if age <=0:
        raise ValueError("cantnot 0")
    return 10 /age

try:
    caculate_xfactor(-1)
except ValueError as error:
    print(error)