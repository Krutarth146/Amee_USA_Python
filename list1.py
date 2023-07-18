# List : Ordered (Indexed), Allows Duplicates, Mutable(Changeble)

list1 = [12, 90.78, 7+8j, 'D', "Krutarth", True, 90.78, 12, [10,20,30,40]]

print(list1)  # [12, 90.78, (7+8j), 'D', 'Krutarth', True, 90.78, 12]
print(type(list1))  # <class 'list'>

print(len(list1))  # 9  # length starts from 1

# Indexing and Slicing
print(list1[3])  # D  # Index starts from 0
print(list1[-1])  # [10, 20, 30, 40]

print(list1[3:])  # 'D', "Krutarth", True, 90.78, 12, [10,20,30,40]
print(list1[::-1])  # [[10, 20, 30, 40], 12, 90.78, True, 'Krutarth', 'D', (7+8j), 90.78, 12]

list2 = [10,(34,90,78,78),False]
print(list1 + list2)  # [12, 90.78, (7+8j), 'D', 'Krutarth', True, 90.78, 12, [10, 20, 30, 40], 10, (34, 90, 78, 78), False]


# List Operations

list1 = [10, 90, 89, 78, 89, 90, 67, 90]
tup1 =  (10, 90, 89, 78)

print(list1.__sizeof__())  # 72  (Consumes More memory)
print(tup1.__sizeof__())   # 56

list1 = list(set(list1))
print(list1)  # [67, 10, 78, 89, 90]


# List Methods
lst1 = [90, 89, 78, 78.9]
lst1[3] = "Dev"
print(lst1)  # [90, 89, 78, 'Dev']

lst1.append(True)
print(lst1)  # [90, 89, 78, 'Dev', True]

# lst1.extend("Krutarth")
# print(lst1)  # [90, 89, 78, 'Dev', True, 'K', 'r', 'u', 't', 'a', 'r', 't', 'h']


lst2 = [10,90,89]
lst1.extend(lst2)  # Don't allow Int
print(lst1)  # [90, 89, 78, 'Dev', True, 10, 90, 89]
print(len(lst1))  # 8

# lst1.append(lst2)   
print(lst1)  # [90, 89, 78, 'Dev', True, [10, 90, 89]]
print(len(lst1))   # 6

lst1.remove("Dev")   # Removes specific element
print(lst1)  # [90, 89, 78, True, 10, 90, 89]

lst1.pop()  # removes last digit
print(lst1)  # [90, 89, 78, True, 10, 90]

lst1.pop()
print(lst1)  # [90, 89, 78, True, 10]
lst1.pop()
print(lst1)  #[90, 89, 78, True]

lst1.pop(2)   # removes specific index element
print(lst1)   # [90, 89, True]

print(lst1.index(True))  # 2
print(lst1.count(90))  # 1


#--------------------------- Copy Method
lst2 = lst1.copy()   # aadhar card copy
print(lst2)

lst3 = lst1

lst1.append(500)

print(lst2)  # [90, 89, True]
print(lst3)  # [90, 89, True, 500]

if lst1 is lst3:
    print("lst1 is lst3 Reference same")

if lst1 is lst2:
    print("lst1 and lst2 are different")

print(id(lst1))  # 2117009986176
print(id(lst2))  # 2117005530816
print(id(lst3))  # 2117009986176