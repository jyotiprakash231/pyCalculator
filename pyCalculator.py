def sum(firstNumber,secondNumber):
    return firstNumber+secondNumber
def Sub(firstNumber,secondNumber):
    return firstNumber-secondNumber
def mul(firstNumber,secondNumber):
    return firstNumber*secondNumber
def div(firstNumber,secondNumber):
    return firstNumber/secondNumber


print("**********pyCalculator**********")
choice=int(input("\n1.Sum\n2.Sub\n3.Mul\n4.Div\nEnter your choice:"));
firstNumber=int(input("\nEnter first number:"))
secondNumber=int(input("\nEnter second number:"))
if choice==1:
    sum(firstNumber,secondNumber)
elif choice==2:
    sub(firstNumber,secondNumber)
elif choice==3:
    mul(firstNumber,secondNumber)
elif choice==4:
    div(firstNumber,secondNumber)
else:
    print("Please input valid choice")
