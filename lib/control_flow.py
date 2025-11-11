#!/usr/bin/env python3

def admin_login(username, password):
    if username=="admin" and password == "12345":
        return "Access Granted"
    elif username == "ADMIN" and password == "12345":
        return "Access Granted"
    else:
        return "Acces Denied"
    # your code here
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "it's brisk out there!"
    elif 40 <= temperature <= 65:
        return "it's a little chilly out there!"
    elif temperature >= 85:
        return "it's too dang hot out there!"
    else:
        return "perfect"
      
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