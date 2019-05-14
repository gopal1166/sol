class A:
    """
    """
    a = 10
    def aFunc(self):
        """
        """
        print("This is class A")
    
class B:
    """
    """
    b = 10
    def bFunc(self):
        """
        """
        print("This is class B")

class C(A, B):
    """
    """
    c = 10
    def cFunc(self):
        """
        """
        print("This is class C")

# create a new object instancwe
instance =  C()

print(instance.c)
instance.cFunc()
    
    
print(instance.b)
instance.bFunc()

print(instance.a)
instance.aFunc()

print("\n--------------------------------------------------")

class MyA:
    """
    """
    def getName(self):
        print("This is class A")

class MyB(A):
    """
    """
    def getName(self):
        print("This is class B")

# create new instance
myinstance = MyB()

myinstance.getName()


print("\n---------------------------------------------")

class MethodOverloading:
    """
    This is method overloading
    """
    def myFunc(self):
        """
        """
        print("This is a func without paramets")

    def myFunc(self, name=None):
            """
            """
            print("This is a func with name parameter")

    def myFunc(self, name=None, age=None):
        """
        """
        print("This is a func without paramets name and age")

# create isntance
instance2 = MethodOverloading()
instance2.myFunc("gopal", 30)

# instance2.myFunc("gopal")



















