from time import sleep 

name = input("What is your name?\n")
age = int(input("How old are you\n"))
sport = (input("What sport do you play\n"))
number = int(input("What is your favorite number\n"))


myAge = 67
print (f"Your name is hideous I'm suprised your parents named you that")
    sleep(3)
if age <= myAge:
    print(f"Man if you aren't younger than me you're an unc") 
    sleep(3)
else:
    print(f"Youngling why are you so young and why are you even using my code?")
    sleep(3)

if sport == "soccer":
    print(f"You are the goat w sport")
    sleep(2)
elif sport == "football":
    print(f"You are a bum")     
    sleep(2)
elif sport == "hockey":
    print(f"You use a stick to put a black disc in a goal what kinda sport is that")
    sleep(2)
elif sport == "baseball":
    print(f"I don't like you and your ice cream scoop hair")
    sleep(2)


if number != 67:
    print(f"Why is 67 not your favorite number you absolute freak")
    sleep(1)
else:
    print(f"I'm so happy your favorite number is 67 you are the goat")
    sleep(1)