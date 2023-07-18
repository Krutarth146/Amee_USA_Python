a=10
print(type(a))  # <class 'int'>

b = 90.89
print(type(b))  # <class 'float'>

c= 5000000000000000000000000000000.90
print(type(c))   # <class 'float'>

d = 'Dev'
print(type(d))  # <class 'str'>

e = True
print(type(e))  # <class 'bool'>

f = 2 + 4j
print(type(f))  # <class 'complex'>

# e = 10
e = 10
print(f+e)  # (2+14j)

h = [1,2,67.90, "Diya", False, 4+9j, [5,6,7]]
print(h)  # [1, 2, 67.9, 'Diya', False, (4+9j), [5, 6, 7]]
print(type(h))  # <class 'list'>

e = (34, "Victus", 90.89, True, (2,3,4,5))
print(type(e))  # <class 'tuple'>

j = {4,5,6,23,90.89}
print(type(j))  # <class 'set'>

k = {'Name' : "Krutarth", "Roll" : 896, "Hobby" : ['cricket', 'dancing', 'cooking']}
print(type(k))  # <class 'dict'>

o = "Chaudhry"
print(type(o))  # <class 'str'>

a= 90
print("Hello Dev",a)

b = 9008
print("Hello Dev",a,"Hello Diya",b) # Hello Dev 90 Hello Diya 9008

# print(a+b,end='\b')
# print("hello")
print(a+b,end='')
print("hello")


print("Hello",'Victus','Diya',sep=' Dhrav ')   # Hello,Victus,Diya

# print("Dev was %born on \"wednesday\'.")  # Dev was %born on "wednesday'.

print('''Hello this is royal
        Gnr Branch 
        near Reliance Chokdi
        near Reliance Chokdi
        near Reliance Chokdi
        near Reliance Chokdi
        Sarghasan Branch''')

# #         # Hello this is royal
# #         #         Gnr Branch
# #         #         near Reliance Chokdi
# #         #         Sarghasan Branch

# # '''
# # Multi 
# # Line
# # Comment
# # '''

# # # Single Line Comment

# # print("Hello""Dev")   # HelloDev
# # print("Hello","Dev")   # Hello Dev


# # # TypeCasting
# # # Convert one Datatype to another datatype

x = 10.99
print(int(x))

x = "10"
print(int(x))

# # print(x)

# programmer = "I like C and Py\n"

# print(5*programmer)



a = 90
b = 801
c = 3300

# if a > b:
#         print(a)
# else:
#         pass


max = a if a>b else b   # Ternary Operator  (HW. - Compare 3 variables and find Greatest one)
print(max)



