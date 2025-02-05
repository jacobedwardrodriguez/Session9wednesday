def greet():
    """
    Simple function that just reads hello
    :return: None
    """
    print("Hello!")

# doc strings are a NECESSARY inclusion for project.

def greet2(name):
    """
    Simple function that greets a person
    :param name: The name of a person
    :return: None
    """
    print(f"Hello, {name}")

greet2("Jane")
greet2("Mary")

def special_op(a=1, b=1):
    """
    Special op is 10xa+b
    :param a: first number
    :param b: second number
    :return: value, 10a+b
    """
    result = 10*a+b
    return result

print(special_op(10,2))
print(special_op(2, 10))
result = special_op(8, 9)
print(f"the special op for 8 and 9 is: {result}")

# print(special_op(b=8,a=9)) *reverse order
print(special_op())
print(special_op(a=9))

def bond_greet(name):
    print(f"The name is: {name}")

def bondise_name(first_name="James", last_name="Bond"):
    return f"{last_name}, {first_name}, {last_name}"

print(bondise_name("John", "Doe"))
bond_greet(bondise_name(first_name="John", last_name="Doe"))
bond_greet(bondise_name())

