# class FirstClass:
#     """
#     This is my first class    
#     """
#     name = "Sol"

#     def func1(self):
#         print("My name is ", self.name)

# # To access the properties and functions of the class

# # creating a new instance of the object
# instance = FirstClass()

# # using this instance  we can access all the properites and fucntions of the class
# print(instance.name)

# # accessing the function of the class
# # print(instance.func1)
# instance.func1()

# --------------------------------------------------------
# using constructor:

# class SecondClass:
#     """
#     SecondClass using constructor
#     """
#     def __init__(self, name, age):
#         """
#         Connstructor function
#         """
#         self.name = name
#         self.age = age

#     def getNameAge(self):
#         """
#         accessing the variables
#         """
#         print("Name, age are: ", self.name, self.age)

# # create isntance with default values
# instance = SecondClass("Sol", 20)

# # accessing the getNameAge() 
# instance.getNameAge()

# # accessing constructor variables
# print(instance.name)

# updating global variable inside of the function using global keyword
name = "Gopal"
def newFunc():
    """
    """
    global name
    name = "Sol"
    print("My name is: ", name)

newFunc()
print("Name outside the function: ", name)
