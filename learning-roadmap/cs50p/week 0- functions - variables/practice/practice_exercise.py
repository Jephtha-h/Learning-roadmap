# CS50P Week 0 - Functions Mastery Practice
# This file contains all function concepts from CS50P Week 0
# Use this for practice and reference

"""
🎯 CORE CONCEPTS MASTERED:
- Parameters vs Arguments
- Position-based Matching  
- Function Scope
- Return vs Print
- Default Parameters
"""

print("=== CS50P WEEK 0 FUNCTIONS MASTERY ===\n")

# =============================================================================
# Q1: PARAMETER vs ARGUMENT IDENTIFICATION
# =============================================================================

print("1. PARAMETER vs ARGUMENT")

def greet(person, message):
    print(f"{message}, {person}!")

name = "Alice"
greet(name, "Hello")

"""
PARAMETERS: person, message (variables in function definition)
ARGUMENTS: name ("Alice"), "Hello" (values passed to function)

Explanation: 
- Parameters are the empty slots in the function header
- Arguments are the actual values passed when calling the function
"""

# =============================================================================
# Q2: POSITION-BASED MATCHING
# =============================================================================

print("\n2. POSITION-BASED MATCHING")

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

describe_pet("Max", "dog")

"""
Output: "I have a Max named dog"

Explanation:
- Computer matches by POSITION, not meaning:
  - First argument "Max" → First parameter animal
  - Second argument "dog" → Second parameter name
- Function follows its internal template regardless of argument meanings
"""

# =============================================================================
# Q3: NAME INDEPENDENCE
# =============================================================================

print("\n3. NAME INDEPENDENCE")

def calculate_area(width, height):
    return width * height

w = 5
h = 10
result = calculate_area(w, h)
print(f"Area: {result}")

"""
Why this works: POSITION matters, not names
- w (5) → First parameter width
- h (10) → Second parameter height  
- Parameter names inside function are independent of variable names outside
"""

# =============================================================================
# Q4: SCOPE CHALLENGE
# =============================================================================

print("\n4. SCOPE CHALLENGE")

def make_juice(fruit):
    drink = f"{fruit} juice"
    return drink

ingredient = "apple"
beverage = make_juice(ingredient)
print(f"Beverage: {beverage}")

# print(drink)  # THIS WOULD CAUSE ERROR - drink doesn't exist outside function

"""
Scope Explanation:
- Variable 'drink' only exists INSIDE the function
- When function ends, 'drink' is destroyed
- We can only access the RETURNED value through 'beverage'
"""

# =============================================================================
# Q5: VALUE TRACING WITH SWAP
# =============================================================================

print("\n5. VALUE TRACING WITH SWAP")

def swap_items(first, second):
    return f"{second} then {first}"

item1 = "eggs"
item2 = "milk"
output = swap_items(item1, item2)
print(f"Output: {output}")

"""
Step-by-step:
- first = "eggs" (first argument → first parameter)
- second = "milk" (second argument → second parameter)  
- Return template f"{second} then {first}" becomes "milk then eggs"
- Function swaps the order of inputs in output
"""

# =============================================================================
# Q6: DEFAULT PARAMETERS
# =============================================================================

print("\n6. DEFAULT PARAMETERS")

def order_coffee(size, type="latte"):
    return f"One {size} {type}"

result1 = order_coffee("large")
result2 = order_coffee("medium", "cappuccino")

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")

"""
Default Parameters Explanation:
- First call: Only one argument provided, so 'type' uses default "latte"
- Second call: Both arguments provided, so 'type' gets "cappuccino"
- Default values provide fallback when arguments aren't provided
"""

# =============================================================================
# BONUS: RETURN vs PRINT DEMONSTRATION
# =============================================================================

print("\n7. RETURN vs PRINT DEMONSTRATION")

def with_return(x):
    result = x * 2
    return result  # Gives value back

def with_print(x):
    result = x * 2  
    print(result)   # Just displays, doesn't give back

print("With return (can store result):")
value1 = with_return(5)
print(f"Stored value: {value1}")

print("\nWith print (cannot store result):")
value2 = with_print(5)  # value2 will be None
print(f"Stored value: {value2} (None because nothing was returned)")

"""
Key Difference:
- RETURN: Gives the value back to caller (can store in variable)
- PRINT: Just displays value on screen (cannot capture it)
"""

# =============================================================================
# PRACTICE: TRY THESE YOURSELF
# =============================================================================

print("\n" + "="*50)
print("PRACTICE EXERCISES - TRY THESE YOURSELF!")
print("="*50)

"""
Practice 1: Fix this broken function call
def introduce(name, age, city):
    print(f"Hi, I'm {name}, {age} years old from {city}")

introduce("New York", 25, "Alice")  # Wrong order!
"""

"""
Practice 2: Write a function that:
- Takes two numbers
- Returns their sum and product as a string
- Has default values of 0 for both parameters
"""

"""
Practice 3: Identify the scope issue:
def create_email(username, domain):
    email = f"{username}@{domain}"
    return email

user = "john"
mail_server = "gmail.com"  
address = create_email(user, mail_server)
print(email)  # What happens here?
"""

print("\n=== END OF CS50P WEEK 0 PRACTICE ===")

"""
🎓 KEY TAKEAWAYS SUMMARY:

1. PARAMETERS = Function inputs (empty slots)
2. ARGUMENTS = Actual values passed to functions  
3. POSITION MATTERS - Computer matches by order, not names
4. SCOPE - Variables inside functions are separate from outside
5. RETURN gives values back, PRINT just displays them
6. DEFAULT PARAMETERS provide fallback values

Remember: Practice makes perfect! Keep experimenting with these concepts.
"""

# =============================================================================
# SOLUTIONS (Comment out when practicing)
# =============================================================================

"""
Practice 1 Solution:
introduce("Alice", 25, "New York")  # Correct order!

Practice 2 Solution:
def calculate(a=0, b=0):
    return f"Sum: {a+b}, Product: {a*b}"

Practice 3 Solution:
print(email) would cause ERROR - email only exists inside the function
We should print(address) instead!
"""