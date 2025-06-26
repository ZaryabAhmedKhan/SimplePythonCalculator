n = float(input("Enter Number: "))
op = input("Enter operator (+,-,*,/): ")
n2 = float(input("Enter Number: "))
if op == '+':
    # result = n+n2
    # print("Result: ", result) you can do it using this method.
    print("Result:",n+n2)
elif op == '-':
    print("Result:",n-n2)
elif op == '*':
    print("Result:",n*n2)
elif op == '/':
    if n2 != 0:
     print("Result: ",n/n2)
    else:
       print("Error, Divison by zero")
else:
    print("Invalid operator")

    