print(ord('A'))   # 65
print(chr(66))   # B

dev = "ROyal is GOod_Institute123."

print(dev[-3:-10:-3])  # 2ti


# String Methods------------------------------------------

str1 = "Hello_My name Is Priyank Modi"


print(str1.count('Is'))  # 1
print(str1.count('i',15))  # 2

print(str1.capitalize())  # Hello_my name is priyank modi

print(str1.casefold())   # hello_my name is priyank modi

# print(str1)
print(len(str1))  # 29  # Length Start from 1 , Index starts from 0
print(str1.center(50,'*'))  # **********Hello_My name Is Priyank Modi***********

print(str1.upper())  # HELLO_MY NAME IS PRIYANK MODI
print(str1.lower())  # hello_my name is priyank modi

print(str1.swapcase()) # hELLO_mY NAME iS pRIYANK mODI
print(str1.title())  # Hello_My Name Is Priyank Modi

print(str1.find('Dev'))  # If str is not found then it returns -1   # -1
# print(str1.index('Dev')) # If str is not found then it generates error  # Error
print(str1.index('H'))  # 0

print(str1.encode())   # Dev Patel -> rtw_odiaq -> Dev Patel

# b'Hello_My name Is Priyank Modi'

str2 = "Ståle"
print(str2.encode())  # b'St\xc3\xa5le'
print(str2.encode(encoding="ASCII", errors = "backslashreplace"))  # b'St\\xe5le
print(str2.encode(encoding="ASCII", errors = "xmlcharrefreplace"))  # b'St&#229;le'
print(str2.encode(encoding="ASCII", errors = "namereplace"))  # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'
print(str2.encode(encoding="ASCII", errors = "ignore"))  # b'Stle'
print(str2.encode(encoding="ASCII", errors = "replace"))  # b'St?le'

print(str2.endswith('t',0,2))   # True

str1 = "Hello_My\tname Is Priyank Modi"
print(str1.expandtabs(16))   # Hello_My        name Is Priyank Modi

list1 = []
list2 = []
for i in range(1,2001):
    if i % 4 == 0:
        # list1.append(i)
        print(i)
    if i%400==0 and i% 100==0:
        # list2.append(i)
        # print(i)
        pass
    elif (i % 4 ==0) and (i % 100 != 0):
        # list2.append(i)
        print(i)
# print(len(list1))
# print(len(list2))

# for i in zip(list1,list2):
#     print(i)

