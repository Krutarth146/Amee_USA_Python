# num = int(input("Enter the value of a: "))    # 
# if num == 9:      # Gives error
#     print(f"{num} is Nine")
# elif num>=9:
#     print(f"{num} is greater than 9")
# else:
#     print(f"{num} is lesser than 9")

# # ----------------------------------

# a = input("Enter the value of a: ")  # str
# b = input("Enter the value of b: ")  # str

# c = int(a) + int(b)
# print(c)


# --------------------------------

a = 90
b = 453
c = 1110

if a > b:
    if a > c:
        print('a is Max')
    else:
        print("c is max")
else:
    if b > c:
        print('b is Max')
    else:
        print("c is max")


# Loops---------------

# Entry Control Loops
# 1. while()
# 2. for

_ = 1
while _ <= 100:  # 100
    print(_,end='\t')   # 100
    _+=1   # 101
print(_)   # 101


print()

# Reverse Number in range
_ = 100
while _ >= 1:  # 100
    if (_ % 5 == 0 or _ % 7 == 0) and _ % 10 ==0:   # Logical and , or        and -> 1 1 = 1
        print(_,end=' ')   # 25 23 21 19 17 15 13 11 9 7 5 3 1
    _-=1   
# print(_)   # 0




# -----Reverse Number print

num = int(input("Enter One Number: "))  # 841  ->  148

while num != 0:    # 841 % 10 = 1
    remainder = num % 10   # 8
    print(remainder,end='')   # 148
    num = num // 10   # 0


# Sum of digits
# Store the reverse Number
# Num and reverse is same or not???
