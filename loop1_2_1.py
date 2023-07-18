num = int(input("Enter one Number: "))

# print(num)
# print(type(num))   # <class 'str'>

# num = 562  ->  265 if same then it is called palindrome
rev = 0
safe = num
while num != 0:   # 782   ->  287
    remainder = num % 10    # remainder = 7
    rev = (rev * 10) + remainder   # rev = 287
    num = num // 10   # num = 0

print(rev)

if safe == rev:
    print(f"{safe} is Palindrome Number")
else:
    print(f"{safe} is Not Palindrome Number")