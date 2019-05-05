# Session 1 : Python: basics

Date: 5/5/2019

local variable:
```
defined inside the function
scope: inside the function
we can't access out side of function
```

globalvar:
```
defined outside of function
sope: global
we can access anywhere in the file (inside the funct as well)
```

arrays:
```
syntax:
arr1 = [1, 2, 3]
names = ["Gopal", "Sol", 2, 4]

accessing using index
names[0]

updating the values
names[0] = "Ram"
```


Tuple:
```
what is the difference b/n list and tuple
immutable: we can t update the value once defined

syntax:
tuple1 = (1, 2, 3)
```

set:
```
what's the difference b/n set and list
diff: set does'nt contains duplicates elements
syntax:
set1 = {1, 2, 3}

to convert list to set:
method: set(list)

eg:
list1  = [1, 2, 2, 3, 3]

mySet = set(list1)
```

dictionay:
```
syntax:
dict = {key: value}

eg:
dict = {
    name: "Gopal",
    sal: 200
}

accessing value from the dict using key
dict[sal]
```

operators:
```
conditional:
assignment:  =
arithmetic: +, - , *, / , %
logical: &&, ||
comparison: >, <, >=, <=, ==
bitwise
```

conditions:
```
if
if else
if elif else   // elseif
```

```
if:
syntax:
if condition:
    statements


if else:
if condition:
    statements
else:
    statements

if elif else:
syntax:
if condition:
    #do something
elif condition:
    #do the stuff
else:
    #do the stuff
```

loops:
```
for, forEach, while, switch

for:
for(initialization, condition, increment/decrement) {
    #code
    
}
```

while:
```
initialize
while condition:
    statement
    incremet/decream
```

