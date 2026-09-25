import math

print("EX1---------")
r = input("nhap r: ")
print(r)
a = math.pi * float(r)
print("Circle area = ", f"{a:.3f}")
print("EX2---------")

c = input("nhap do C: ")
F = float(c) * 1.8 + 32 
print("Fahrenheit = ", f"{F:.3f}")
print("EX3---------")

def is_prime(n):
    if(n <= 1) : return False
    if(n == 2) : return True
    if(n % 2 == 0) : return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if(n % i == 0): return False
    return True
try:
    n = int(input("nhap so nguyen: "))
    if is_prime(n):
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} kh la so nguyen to")
except ValueError:
    print("nhap dung so nguyen nhe!")
    
print("EX4--------")
def is_perfect(n):
    if(n <= 1): return False
    sum = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n % i == 0):
            sum += i
            if i != n // i :
                sum += n // i
    return sum == n
a = int(input("nhap a:"))
for i in range( 0,  a):
    n = int(input(f"nhap so thu {i + 1}:"))
    print(f"ket qua ktra {n}: {is_perfect(n)}")


print("EX5--------")
colors = ["red", "blue", "yellow", "pink", "grey"]
color = input("What is your favorite color?")
if color in colors :
    print(f"Your color is at index {colors.index(color)} in my list")
else:
    print("Sorry, I could not find your color")

    
print("EX6--------")
range1 = range(0,7)
range2 = range(1,11,3)
range3 = range(5,0,-1)
range4 = range(6,-3,-2)
print("range1:", *range1)
print("range2:", *range2)
print("range3:", *range3)
print("range4:", *range4)

print("EX7---------")
def remove_dollar_sign(s):
    return s.replace("$", "")
print(remove_dollar_sign("$Hello $World$"))

print("EX8---------")
def extract_even(list):
    even = []
    for x in list:
        if x % 2 == 0:
            even.append(x)
    return even
print(extract_even([1, 4, 5, -1, 10]))

print("EX9----------")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

print("EX10---------")
def divisors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end = " ")
print(divisors(18))

print("EX11---------")
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(distance(1, 2, 4, 6))

print("EX12---------")
def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

print_pattern(4, 5)
