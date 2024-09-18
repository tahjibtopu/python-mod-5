'''
Module-5 Project-1, a basic calculator; Name: Tahjib
'''

def add(a, b):
    return a+ b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "ValueError: Number cannot be divided by zero"
    return a / b

def mod(a, b):
    return a % b

print("Select options:")
print("1 for Add \n2 for Subtract \n3 for Multiply \n4 for Divide \n5 for Modulus \n")

while True:
    selector = input("Choose 1/2/3/4/5: ")

    if selector in ['1', '2', '3', '4', '5']:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Enter a numeric value")
            continue

        if selector == '1':
            result = add(a , b)
            print(f"{a} + {b} = {result}")
        
        elif selector == '2':
            result = sub(a , b)
            print(f"{a} - {b} = {result}")

        elif selector == '3':
            result = mul(a , b)
            print(f"{a} * {b} = {result}")

        elif selector == '4':
            result = div(a , b)
            print(f"{a} / {b} = {result}")

        elif selector == '5':
            result = mod(a , b)
            print(f"{a} % {b} = {result}")
    
    else:
        print("Please select a valid option")
    
    cont_op = input("Want to continue? (y/n)")

    if cont_op.lower() != "y":
        break