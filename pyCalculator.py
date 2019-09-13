def sum(firstNumber,secondNumber):
    return firstNumber+secondNumber
def sub(firstNumber,secondNumber):
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
    result=sum(firstNumber,secondNumber)
    print(result)
elif choice==2:
    result=sub(firstNumber,secondNumber)
    print(result)
elif choice==3:
    result=mul(firstNumber,secondNumber)
    print(result)
elif choice==4:
    result=div(firstNumber,secondNumber)
    print(result)
else:
    print("Please input valid choice")
