# char a = 'D';

v = ord('A') 
print(v)  # 65

v = ord('f')
print(v)   # 101

g = chr(90)
print(g)  # Z

g = chr(108)
print(g)  # l

x = 90.89
print(type(x))   # <class 'float'>
x = str(x)   # TypeCasting
print(type(x))   # <class 'str'>

# --------------------------String Slicing----------------------------------

str1 = "Dev Bhatt is Good Boy123."
str2 = "Dev1 Bhatt is Good Boy123."
print(type(str1))   # <class 'str'>

print(str1.__sizeof__())   # 74
print(str2.__sizeof__())   # 75

print(id(str1))  # 1783996963920
print(id(str2))  # 1783996964320

str1 = "Dev Bhatt_is Good Boy123."
#       0123456789              -1  # Last Index = (Starts with -1)

# Indexing satrts with 0 and if we want to count from last Index then we need to starts with -1 only.
print(str1[0])  # D
print(str1[3])  #   (space)
print(str1[-3])  # 2
print(str1[-1])  # .
print(str1[-16])  # _
print(str1[9])  # _

# --------------------------------------------------------------
# print(str1[Start Position : End Position (n-1)])
str1 = "Dev Bhatt_is_Good Boy123."
print(str1[0 : 7])   # Dev Bha
print(str1[5 : 13])   # hatt_is_
print(str1[13 : 5])   # 
print(str1[ : 5])   # Dev B
print(str1[3 : ])   #  Bhatt_is_Good Boy123.
print(str1[:])      # Dev Bhatt_is_Good Boy123.
print(str1[-5:-1])  # y123
print(str1[5:0])    #

# -------------------------------------------------
str1 = "Dev Bhatt_is_Good Boy123."

# print(str1[Start : end(n-1) : step(n-1)])
print(str1[2 : 8 : 1])  # default 1   # v Bhat
print(str1[2 : 13 : 2])  # vBati_
print(str1[2 :  : 2])  # vBati_odBy2.
print(str1[2 :  : ])  # v Bhatt_is_Good Boy123.
print(str1[ :  : 1])  # Dev Bhatt_is_Good Boy123.
print(str1[ :  : -1])  # .321yoB dooG_si_ttahB veD
print(str1[ :  : -3])  # .1Bo__a D
print(str1[10 : 2 : -3])  # itB
print(str1[2 : 10 : 3])  # vht
print(str1[2 : 10 : -3])  #    (blank)