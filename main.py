num1=int(input("please pick your first number:"))
num2=int(input("please pick your second number:"))
print("what operation would you like to do")
operation=input ("+,-,/,*")
if operation == ("+"):
  print (num1+num2)
elif operation == ("-"):
  print (num1-num2)
elif operation == ("/"):
  print(num1/num2)
elif operation == ("*"):
  print (num1*num2)
else:
  print ("please try again")