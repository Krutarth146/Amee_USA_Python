list1 = [10,20,30]
print(list1)  # [10, 20, 30]

print(type(list1))   # <class 'list'>

tup1 = ()
print(type(tup1))   # <class 'tuple'>


dict1 = {"Name" : "Arya", 'surname' : "Salecha", 'school' : 'xyz'}
print(type(dict1))   # <class 'dict'>

set1 = {10}
print(set1) # {10}
print(type(set1))   # <class 'set'>


# List ---> Ordered, Allow's Duplicates, Mutable (Changeble) 
list1 = [10,20,30,90,78,45,10,10,10]

# Indexing
print(list1)   # [10, 20, 30, 90, 78, 45, 10, 10, 10]
print(list1[2])  # 30
print(list1[-1])  # 10

# Slicing
# print(list1[start : End (n-1)])

print(list1[1 : 5])   # [20,30,90,78]
print(list1[3 : 4])   # [90]
print(type(list1[3 : 4]))  # <class 'list'>

list1 = [10,20,30,90,78,45,10,10,10]
print(list1[3:1])   # []
print(list1[:5])   # [10,20,30,90,78]
print(list1[2:])   # [30,90,78,45,10,10,10]
print(list1[:])   # [10, 20, 30, 90, 78, 45, 10, 10, 10]
print(list1[-2:-5])   # []
print(list1[-5:-2])   # [78, 45, 10]
print(list1[-2:3:2])   # []


# Matrix

list1 = [[10,89,67], 
         [76,23,42], 
         [23,12,89]]

print(list1)   # [[10, 89, 67], [76, 23, 42], [23, 12, 89]]

a =100
list1[1][1] = 100   # Mutable (Changeble)
list1[1][2] = 100   # Mutable (Changeble)
print(list1)


list1 = [[10,89,67], 
         [76,23,42], 
         [23,12,89]]

print(len(list1))   # 3
for j in list1:   # [10,89,67]
    for k in j:    # k = 10
        print(k,end=' ')   # 10

print()
for i in range(len(list1)):   # 3    i= 0
    for j in range(len(list1[i])): # 3  j = 0
        print(list1[i][j],end=' ')   # list1[2][2]
    print()

print()
for i in range(len(list1)):   # 3    i= 0
    for j in range(len(list1[i])): # 3  j = 0
        print(list1[j][i],end=' ')   # list1[0][0]
    print()

# 10 76 23
# 89 23 12
# 67 42 89

list1 = [[10,89,67], 
         [76,23,42], 
         [23,12,89]]

# 10 89 67 42 23 76 23 12 89



for i in range(len(list1)):
    if i % 2 == 0:
        for j in range(len(list1[i])):
            print(list1[i][j],end=' ')
    else:
        for j in range(len(list1[i])-1, -1,-1):
            print(list1[i][j],end=' ')   # 10 89 67 42 23 76 23 12 89