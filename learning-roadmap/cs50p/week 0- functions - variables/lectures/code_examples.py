
# ========= hello0.py =========
# Demonstrates a function with a positional argument

print("hello, world")

# ========= hello1.py =========
# Demonstrates a function with a positional argument and a return value

name = input("What's your name? ")
print("hello,")
print(name)

# ========= hello2.py =========
# Demonstrates concatenation of strings

name = input("What's your name? ")
print("hello, " + name)

# ========= hello3.py =========
# Demonstrates a function with two positional arguments

name = input("What's your name? ")
print("hello,", name)

# ========= hello4.py =========
# Demonstrates a function with a positional argument and a named argument

name = input("What's your name? ")
print("hello, ", end="")
print(name)

# ========= hello5.py =========
# Demonstrates a format string

name = input("What's your name? ")
print(f"hello, {name}")

# ========= hello6.py =========
# Demonstrates str functions

name = input("What's your name? ").strip().title()
print(f"hello, {name}")

# ========= hello7.py =========
# Demonstrates str functions

name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")

# ========= hello8.py =========
# Demonstrates defining a function without parameters


def hello(): # type: ignore
    print("hello")


name = input("What's your name? ")
hello()
print(name)

# ========= hello9.py =========
# Demonstrates defining a function with a parameter


def hello(to): # type: ignore
    print("hello,", to)


name = input("What's your name? ")
hello(name)

# ========= hello10.py =========
# Demonstrates defining a function with a parameter with a default value


def hello(to="world"): # type: ignore
    print("hello,", to)


hello()
name = input("What's your name? ")
hello(name)

# ========= hello11.py =========
# Demonstrates defining a main function


def main(): # type: ignore
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


main()


# ========= calculator0.py =========
# Demonstrates addition

x = 1
y = 2

z = x + y

print(z)

# ========= calculator1.py =========
# Demonstrates (unintended) concatenation of strings

# Prompt user for two integers
x = input("What's x? ")
y = input("What's y? ")

# Print sum
z = x + y
print(z)

# ========= calculator2.py =========
# Demonstrates conversion from str to int

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)

# ========= calculator3.py =========
# Demonstrates nesting of function calls

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x + y

print(z)

# ========= calculator4.py =========
# Demonstrates conversion of str to float

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x + y

print(z)

# ========= calculator5.py =========
# Demonstrates rounding to nearest int

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(z)

# ========= calculator6.py =========
# Demonstrates fewer variables

x = float(input("What's x? "))
y = float(input("What's y? "))

print(round(x + y))

# ========= calculator7.py =========
# Demonstrates formatting with commas

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")

# ========= calculator8.py =========
# Demonstrates division

x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)

# ========= calculator9.py =========
# Demonstrates rounding after the decimal point

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)

# ========= calculator10.py =========
# Demonstrates formatting after the decimal place

x = int(input("What's x? "))
y = int(input("What's y? "))

z = x / y

print(f"{z:.2f}")

# ========= calculator11.py =========
# Demonstrates defining a function with a return value


def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
