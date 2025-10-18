def add(P, Q):
    return P + Q

def substract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P/Q

print("Please select the operation:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice = str(input("Select a/b/c/d"))
num1 = int(input("Write first number:"))
num2 = int(input("Write second number:"))
if choice == "a":
    print(num1,"+",num2, "=", add(num1, num2))
elif choice == "b":
    print(num1,"-",num2, "=", substract(num1, num2))
elif choice == "c":
    print(num1,"*",num2, "=", multiply(num1, num2))
elif choice == "d":
    print(num1,"/",num2, "=", divide(num1, num2))
else:
    print("Invalid choice")