def sum(firstNumber,secondNumber):
    return firstNumber+secondNumber


<<<<<<< HEAD
=======

>>>>>>> b73489d1ef2c3f1b7394b0a1fa34bf93e89add68
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
