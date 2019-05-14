# Session 5 : Python basics: multiple inheritance, method overriding

Date: 13/5/2019:

multiple inheritance

syntax:
```
one class can inherit many classes

class A:
    pass
class B:
    pass

class C(A, B):
    pass
```

Method overriding:

flow:
```
parent, child class
define functions with the same name in both classes
```

syntax:
```
class A:
    def myFunc(self):
        statements

class B:
    def myFunc(self):
        statements
```

Method overloading:

Python doesn't support method overloading, but we can use though the latest defined function

flow:
```
in one class
define a function n give parameters

define another func with same name n define different paramters

we can call this fucntion in many ways
```

syntax:
```
class A:
    def myFunc(self):
        pass
    
    def myFunc(self, name):
        pass

    def myFunc(self, name, age):
        pass

```
























