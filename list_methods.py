list1 = [10,90,89,43,56,78,32]


# Indexing
print(list1[1])  # 90
print(list1[-1])  # 32
print(type(list1[-1]))   # <class 'int'>

list2 = [10,20,30,([{'name' : "Krutarth", 'address' : {'city' : 'Ahm', 'pincode': [10,90,56,78,43]}}])]
# print(list2[-1][0])   # {'name': 'Krutarth', 'address': {'city': 'Ahm', 'pincode': [10, 90, 56, 78, 43]}}
# print(list2[-1][0]['address'])   # {'city': 'Ahm', 'pincode': [10, 90, 56, 78, 43]}
# print(list2[-1][0]['address']['pincode'])   # [10, 90, 56, 78, 43]
# print(list2[-1][0]['address']['pincode'][-2])   # 78

print(type(list2[-1]))   # <class 'list'>
print(type(list2[-1][0]))   # <class 'dict'>

# SLicing

list1 = [10,90,89,54,67,32,45,112,3,4,665,343,32]
print(list1[1:5])   # [90, 89, 54, 67]


# print(list1[start : end (n-1) : step(n-1)])

print(list1[4:5:-1])    # []
print(list1[-5::2])    # [3, 665, 32]
print(list1[-5:-1:2])    # [3, 665]
print(list1[5::-3])    # [32, 89]
print(list1[5:9:2])    # [32, 112]
print(list1[::1])    #  [10,90,89,54,67,32,45,112,3,4,665,343,32]
print(list1[::-1])    # [32, 343, 665, 4, 3, 112, 45, 32, 67, 54, 89, 90, 10]
print(list1[-5:-7:1])    # []
print(list1[3:-6:])    # [54, 67, 32, 45]
print(list1[-3:5:2])    # []

for i in range(-3,5,2):
    print(i)  # -3, -1, 1, 3

# List Methods

list1.append("Amee")
list1.append(True)

print(list1)   # [10, 90, 89, 54, 67, 32, 45, 112, 3, 4, 665, 343, 32, 'Amee', True]

list1.extend("Dev")
print(list1)   # [10, 90, 89, 54, 67, 32, 45, 112, 3, 4, 665, 343, 32, 'Amee', True, 'D', 'e', 'v']

l4 = [10,90,89]

# list1.append(l4)
# list1.extend(556)  # int object is not iterable
print(list1)   # [10, 90, 89, 54, 67, 32, 45, 112, 3, 4, 665, 343, 32, 'Amee', True, 'D', 'e', 'v', [10, 90, 89]]

# list1.extend(l4)
# print(list1)   # [10, 90, 89, 54, 67, 32, 45, 112, 3, 4, 665, 343, 32, 'Amee', True, 'D', 'e', 'v', 10, 90, 89]


del list1[5:]

print(list1)   # [10, 90, 89, 54, 67]

# list1.insert(2, 400)
# print(list1)   # [10, 90, 400, 89, 54, 67]
# list1.insert(-1, 300)
# print(list1)   # [10, 90, 400, 89, 54, 300, 67]
# list1.insert(0, 300)
# print(list1)   # [300, 10, 90, 400, 89, 54, 300, 67]

# ele = list1.pop()
# ele = list1.pop()
# print(ele) # 67


# ele1 = list1.pop(0)
# print(list1)  # [90, 89]


# list1.remove(90)
# print(list1)   # [89]

list1.reverse()
print(list1)   # [67, 54, 89, 90, 10]

# list1.sort()
list1.sort(reverse=True)

print(list1)  # [90, 89, 67, 54, 10]

l5 = [10,90,89,43,56,32,11,78,65,43,32]

for k in l5:
    print(k)

# for j in range(len(l5)):
#     # print(j)  
#     print(l5[j],end =' ')   # 10 90 89 43 56 32 11 78 65 43 32

# print()
# for h in l5[::-1]:
#     print(h,end=' ')   # 32 43 65 78 11 32 56 43 89 90 10

    

# print()
# for h in reversed(l5):
#     print(h,end=' ')   # 32 43 65 78 11 32 56 43 89 90 10
    

# print()
# for h in range(len(l5)-1, -1, -1):
#     print(l5[h],end=' ')   # 32 43 65 78 11 32 56 43 89 90 10



l5 = [10,90,89,43,56,32,11,78,65,43,32]

for j in range(len(l5)):
    for k in range(j+1,len(l5)):
        if l5[j] > l5[k]:
            l5[j],l5[k] = l5[k],l5[j]

print(l5)  # [10, 11, 32, 32, 43, 43, 56, 65, 78, 89, 90]

l1 = [10, 11, 32, 32, 43]

# [[10,10], [10,11], [10,32], [10,32], [10,43]....]
matrix = []

for i in l1:
    for j in l1:
        matrix.append([i,j])

print(matrix)  # [[10, 10], [10, 11], [10, 32], [10, 32], [10, 43], [11, 10], [11, 11], [11, 32], [11, 32], [11, 43], [32, 10], [32, 11], [32, 32], [32, 32], [32, 43], [32, 10], [32, 11], [32, 32], [32, 32], [32, 43], [43, 10], [43, 11], [43, 32], [43, 32], [43, 43]]


l3 = [20, 90, 20, 40, 32, 11,90,90]

print(l3.index(20))  # 0
print(l3.index(20, 1))  # 2



print(l3.count(20))  # 2
print(l3.count(90))  # 3
print(l3.count(90))  # 3


l4 = l3.copy()   # Xerox Copy   # Shallow Copy

l5 = l3   # Digilocker  # Deep Copy


l3.append(100)
l5.append(200)

print(l3,l4,l5)  # [20, 90, 20, 40, 32, 11, 90, 90, 100, 200] [20, 90, 20, 40, 32, 11, 90, 90] [20, 90, 20, 40, 32, 11, 90, 90, 100, 200]


l3 = [20, 90, 20, 40, 32, 11,90,90]
# 20 ---> [0,2]
# 90 ---> [1,6,7]


unique = []


for i in l3:
    if i not in unique:
        unique.append(i)

print(unique)   # [20, 90, 40, 32, 11]

for ele in unique:
    temp = []
    for ind in range(len(l3)):
        if ele == l3[ind]:
            temp.append(ind)
    print(ele,'--->',temp,end='  ')   # 20 ---> [0, 2]  90 ---> [1, 6, 7]  40 ---> [3]  32 ---> [4]  11 ---> [5]