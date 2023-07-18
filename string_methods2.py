str1 = "{}_is {} Institute Ever123.".format('Royal', 'Good')
print(str1)   # Royal_is Good Institute Ever123.

str1 = "{1}_is {0} Institute Ever123.".format('Royal', 'Good')
print(str1)   # Good_is Royal Institute Ever123.

str1 = "{name}_is {mode} Institute Ever123.".format(name='Royal', mode = 'GOod')
print(str1)   # Royal_is GOod Institute Ever123.


# Advanced format Method  (fstring)

a = 90
b = 80

print(f"Sum of {a} and {b} is {a+b}")  # Sum of 90 and 80 is 170


str1 = "Dev Is Good Boy"
str2 = "xyz"
print(str1.isalnum())   # True
print(str1.isalpha())   # True
print(str1.isascii())   # True
print(str1.isdecimal())   # True
print(str1.isdigit())   # True
print(str1.isnumeric())   # True

print(str1.isidentifier())   # True
print(str1.isspace())   # True
print(str1.istitle())  # True


list1 = ['Name', 'roll', 'marks']
p = "9".join(list1)
print(p)


str2 = '_'.join(str1)
print(str2)   # D_e_v_ _I_s_ _G_o_o_d_ _B_o_y


str1 = "        Dev Is Good Boy           "
print(len(str1))   # 15
print(str1.lstrip())   # Dev Is Good Boy
print(str1.rstrip())   #         Dev Is Good Boy


str1 = "Dev_Is Good\nBoy"
print(str1.ljust(20,'*'))   # Dev Is Good Boy*****
print(str1.rjust(20,'9'))   # 99999Dev Is Good Boy

print(str1.partition(' '))   # ('Dev', ' ', 'Is Good Boy')   # Partition into 3 parts
print(str1.rpartition(' '))   # ('Dev Is Good', ' ', 'Boy')

print(str1.split(' '))   # ['Dev', 'Is', 'Good', 'Boy']

print(str1.removeprefix('D'))   # ev Is Good Boy
print(str1.removesuffix('y'))   # Dev Is Good Bo

print(str1.replace('Dev', 'Aman'))   # Aman Is Good Boy

print(str1.split('_'))  # ['Dev', 'Is Good Boy']
print(str1.splitlines())  # ['Dev_Is Good', 'Boy']
print(str1.startswith('e',1))  # True


str1 = "Dev_is good Boy"
print(str1.title())  # Dev_Is Good Boy

str2 = '900'
print(str2.zfill(5))  # 00900


str3 = "Sam is God. xyz"

name = 'Sam'
new_name = 'Ram'
ignore = 'xyz'

table = str3.maketrans(name, new_name, ignore)
print(table)   # {83: 82, 97: 97, 109: 109}


print(str3.translate(table))   # Ram is God.


dict1 = {'name' : "Krutarth", 'gender' : "Male", 'ROll_num' : 90}   # dictionary

str6 = "{name} is {gender}. His roll is {ROll_num}"
print(str6.format_map(dict1))   # Krutarth is Male. His roll is 90


# Tasks
str9 = 'Krutarth Daxeshbhai Patel'

list1 = str9.split(' ')
print(list1)   # ['Krutarth', 'Daxeshbhai', 'Patel']

print(f"{list1[0][0]}.{list1[1][0]}.{list1[2]}")  # K.D.Patel

# Task 2
# count space, vowel , consonents

str7 = "Python Programming"
str7.lower()
vowel = ['a','e','i','o','u']
vowelc = 0
conso = 0
space = 0

for i in str7:
    if i in vowel:   # Membership Operator -> in, not in
        vowelc += 1
    elif i.isspace():
        space += 1
    else:
        conso += 1

print(vowelc) 
print(conso)
print(space)

# task 3

str8 = 'This is the lion in the cage.'

print(str8.replace(' the ', ' ',5))  # This is lion in cage.

str80 = "Keep yourself Mute while not speaking"

str80=str80.replace(' ','_',1)   # Keep_yourself Mute while not speaking
str80 = str80[::-1]
str80 = str80.replace(' ','#',1)
str80 = str80[::-1]   # gnikaeps#ton elihw etuM flesruoy_peeK
print(str80)  # Keep_yourself Mute while not#speaking


import re

input_str = "PYnative29@#8496"
digit_list = [int(num) for num in re.findall(r'\d', input_str)]
print('Digits:', digit_list)

