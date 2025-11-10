a = int(input("Enter the number-1: "))
b = int(input("Enter the number-2: "))

def sum( a,b):
    return a+b
def sub( a,b):
    return a-b
def multi(a ,  b):
    return a*b
def div(a ,b):
    return a/b

print("Addition: ", sum(a,b) )
print("Subtraction: ", sub(a,b) )
print("Multiplication: ", multi(a,b) )
print("Division: ", div(a,b) )