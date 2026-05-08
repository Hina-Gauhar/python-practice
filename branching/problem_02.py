# calculator
num1=int(input("enter a number "))
num2=int(input("enter a number "))
oper=input("what operation u want to perform")

if(oper == "+"):
    print(num1," + ",num2," = ",num1+num2)
elif(oper == "-"):
    print(num1," - ",num2," = ",num1-num2)
elif(oper == "*"):
    print(num1," * ",num2," = ",num1*num2)
elif(oper == "/"):
    print(num1," / ",num2," = ",num1/num2)
elif(oper == "%"):
    print(num1," % ",num2," = ",num1%num2)
elif(oper == "**"):
    print(num1," ** ",num2," = ",num1**num2)
elif(oper == "//"):
    print(num1," // ",num2," = ",num1//num2)
else:
    print("Math error")
