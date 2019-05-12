class X:
    """
    """
    pass

class Parent:
    """
    """
    parentVariable = 0

    def parentFunction(self):
        """
        """
        print("This is parent function")
        pass

class Child(Parent):
    """
    """
    childProperty = 2
    pass 

# print(Child.childProperty)

instance = Child()

# accessing parent property
print(instance.parentVariable)

# accessing parent function
instance.parentFunction()

# to check whether the instance belongs to the class or not
print(isinstance(instance, X))

print("\n------------------------------------------------------")

# multi leve inheritance
class A:
    """
    """
    a = 1

    def aFunc(self):
        """
        """
        print("This is class A")

class B(A):
    """
    """
    b = 2

    def bFunc(self):
        """
        """
        print("This is class B")

class C(B):
    """
    """
    c = 4

    def cFunc(self):
        """
        """
        print("This is class C")

# create instance of class C
cInstance = C()

# class C props, funcs
print(cInstance.c)
cInstance.cFunc()

# class B props, funcs accessing using class C instance
print(cInstance.b)
cInstance.bFunc()

# class A props, funcs 
print(cInstance.a)
cInstance.aFunc()