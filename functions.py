# 1. Pre Defined   -> print(), input(), raw_input() -> python version - 2
# 2. User Defined 

# def - keyword

# 1. Takes nothing and return nothing
# 2. Takes Something and return nothing
# 3. Takes nothing and return Something
# 4. Takes Something and return Something


# 1. Takes nothing and return nothing

# void sum();   // func. declaration

# main()
# {
#     sum();    // func. calling
# }

# void sum()    // func. defination
# {
#     int a=10,b=30;
#     printf("%d",a+b);
# }

list1 = [10,90,89,78]

print(sum(list1))
print(sum(list1)//len(list1))


def add():   # func. defination
    print(10+20)
add()   # func. calling


# 2. Takes Something and return nothing

def Dev(a,b):
    print(a+b)

Dev(10,90)  # 100


# 3. Takes nothing and return Something

def div():
    a,b = 90,45
    return a//b
# print(div())   # 2
x = div()
print(x)

# 4. Takes Something and return Something

def sub(x, y, z):
    return x-y-z

print(sub(90,20,10))  # 60


#---------------------------------------------

def option(p,q,r=0):
    return p + q + r  # 20 + 30 + 15

print(option(20,30, 15))   # 65


def opt1(name1, name2, name3=None):
    print(f"Welcome {name1}, {name2} and {name3}")


opt1("Dev", 'Diya')

x = None
print(type(x))  # <class 'NoneType'>


# ----------------------------------------

def Royal(*args):
    # print(args)
    for _ in args:
        print(_,end=' ')

Royal('Dev', 90, 67.90, True)
print()
def r1(Guru, st_name, *students, Price):
    for y8 in students:
        print(y8,end='  ')

    print(len(students))
    print(Guru)
    print(Price)

r1("Dhiraj_Sir", 500,900,"Tejas Sir", 350000)