#!/usr/bin/env python3

def admin_login(username, password):
    if username=="admin" and password == "12345":
        return "Access granted"
    elif username == "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Acces denied"
    # your code here
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "i=It's a little chilly out there!"
    elif temperature >= 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
      
    # your code here
    pass

def fizzbuzz(num):
    # your code here
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 3 == 0):
        return "Fizz"
    elif (num % 5 == 0):
        return "Buzz"
    else:
        return num
    
    pass

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print ("Invalid operation!")
        return None
    
    pass

print(admin_login("admin","12345"))
print(admin_login("ADMIN","12345"))


print(hows_the_weather(30))
print(hows_the_weather(55))

print(fizzbuzz(0))
fizzbuzz(3)

print (calculator("+",10,5 ))
print(calculator("/",34,9))