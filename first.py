# '''
# a = 90
# print('Hello Amee',a,"Good Morning",end=' Amee ')
# print("This is h1")

# print("""
# dbvdfbfdb
#                 vfdfvdfv
# fdvdfvdf
# dvd""")
# '''

# a = 'sfvdfvdf'

# print(type(a))

# # b = int(input("Enter number: "))
# # print(b)
# # print(type(b))

# # c = 67.90

# d = int(input())
# e = int(input())
# print(d+e)
# print(d-e)
# print(d*e)
# print(d/e)  # Return float
# print(d//e)  # return floor
# print(d%e)

# a = 90
# b = 78
# # area = a*b 
# print(f"Area is {a*b}")

# import csv
# filename = "amee.txt"
# with open(filename,'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow("Hello this is royal")

# 1. Consider this list 
# [1,2,4]
# Create a new list in which each element represents the count of the element in the previous list
# New List - [1, 2, 2, 4, 4, 4, 4]
list1 = [1,2,4]
list2 = []
for i in list1:
    temp = i
    for k in range(temp):
        list2.append(i)
    list2.sort()

print(list2)

# 2. Find the index of unique elements from the list and display those elements
list1 = [3,50,4,5,6,7,23,3,4,5,6]

for i in list1:
    if list1.count(i) == 1:
        print(list1.index(i))

# 3. Write a Python program to remove duplicates from a list. [1, 1, 2, 3, 2] - [1,2,3]

# 4. Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become 3 + 33 + 333 + 3333 + 33333 

# 5. Write a Python function that checks whether a passed string is palindrome or not.
str1 = "Medidem"

def palindrome(str1):
    flag=0
    length = len(str1)
    for i in range(len(str1)):
        if str1[0] == str1[length-1]:
            flag = 1
        else:
            flag = 0
            break

    if flag==1:
        return 1

if palindrome(str1):
    print("Palindrome")
else:
    print("Fail")

# 6. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# 7. Python program to find second largest number in a list.
list1 = [23,90,40,506,80,90,453,70]
list1.sort()
t = list1[-2]
if list1.count(t) > 1:
    for i in list1:
        if i==t:
            print(t)
else:
    print(t)