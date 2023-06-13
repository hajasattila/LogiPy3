# Task 1-2 - Print
print("Welcome", "to", "Logiscool", sep=", ", end="\n_____________\n")
print("You are welcomed here.", end="\n")

a = 42
b = "apple"
c = True
print(a, b, c)
print(str(a) + " " + b + " " + str(c))

# Task 3 - Types
print(type(a))
print(type(b))
print(type(c))

# Task 4 - Integers
print(123)
print(0o123)
print(0x123)
print(bin(123))
print(0b101101)

# Task 5 - Floats
a = 0.0002
b = 2e-4
print(a)
print(b)
print(0.0000000000000000000000001)

# Task 6 - Print special characters
print("""'Learning at Logiscool was the best decision of my life!' - said the wise old man
'And what was your worst decision?' - asked the student
'I could've started younger.'""")

# Task 7 - Operators
try:
    a = int(input("First number:\n"))
    b = int(input("Second number:\n"))
    if a > b:
        print("a=", a, " is greater than b=", b, ".", sep="")
    elif a < b:
        print("b=", b, " is greater than a=", a, ".", sep="")
    else:
        print("a=", a, " and b=", b, " are equal.", sep="")
except:
    print("I can't do this.")

# Task 8 - Priorities
print(5 * 25 % 8 + 100 / 2 * 8 // 2)
print(5 * 25 % (8 + 100 / 2 * 8 // 2))
print(5 * ((25 % 8) + 100) / 2 * 8 // 2)

# Task 9 - Brackets
print(3 + 20 % 4 ** 2 * 5 / 5 - 5)
print((3 + (((20 % (4 ** 2)) * 5) / 5)) - 5)

# Task 10 - Random division error
import random
try:
    for i in range(1, 10):
        a = random.randint(-10, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        d = random.randint(-10, 10)
        e = random.randint(-10, 10)
        print(a/b/c/d/e)
except ZeroDivisionError:
    print("At least one variable was a zero.")
