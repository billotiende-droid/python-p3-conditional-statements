dog_state= ["hungry","thirsty","playful","cuddly","sleepy"]

for dog in dog_state:
        if dog == "hungry":
            owner = "refilling food bowl."
        elif dog == "thirsty":
            owner = "refiling your bowl."
        elif dog == "playful":
            owner = "playin tug-of-war."
        elif dog == "cuddly":
            owner = "snuggling."
        else:
            owner= "reading newspaper."

        print(f"When the dog is {dog} and so the owner is {owner}")


def control_flow(value):
           if value:
            print("yep!")
           else: 
            print("nope")

control_flow(False)    
control_flow(None)   
control_flow(True)
control_flow("")
control_flow(0)
control_flow("0")


age = 1

is_baby = 'baby' if age > 2 else 'not a baby'

print(is_baby)


def divide(num1,num2):
        try:
            quotient= num1 /num2 
            print(quotient)
        except ZeroDivisionError:
            print("Error:num2 cannot be equal to 0")  
        except TypeError:
            print("Eror:input must be of typ int or float")
        finally:
             print("Isn't division fun")


         

divide (10,5)
divide (79,2)
divide (53,6)

