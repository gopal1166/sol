# # create a new file if the file does't exist
# with open('test.txt', 'r') as f:
#     # f.write("Hello")

#     print(f.readline())

#     f.close()



# try:
#     res = 4 / 0
#     # data base operations
# except Exception as error:
#     print("Error: ", error)
# finally:
#     print("finally must be executed")

# res = 4 / 0

# print("last line of code")

arr1 = [1, 2, 3]

for x in arr1:
    print(x ** 2)

# list comprehension: returns new list from the old list
 [x**2  for x in arr1]