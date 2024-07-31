##Excercise 5: Simple Math

def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def mult(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1/n2

def main():
    n1 = int(input("What is the first number? "))
    n2 = int(input("What is the second number? "))
    try:
        if n1*n2 < 0:
            raise ValueError("Do not enter a negative number.")
        else:
            print(f"{n1} + {n2} = {add(n1,n2)}\n"
                f"{n1} - {n2} = {subtract(n1,n2)} \n"
                f"{n1} * {n2} = {mult(n1, n2)}\n"
                f"{n1}/{n2} = {divide(n1, n2)}\n "
            )
    
    except ValueError as e:
        print(e)

main()


