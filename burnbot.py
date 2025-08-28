from time import sleep 

name = input("What is your name?\n")
age = int(input("How old are you\n"))
sport = (input("What sport do you play\n"))
number = int(input("What is your favorite number\n"))
color = input("What is your favorite color?")
candy = input("what is your favorite candy")


myAge = 67
print (f"Your name is hideous; I'm suprised your parents named you that")
sleep(3)
if age <= myAge:
    print(f"Man if you aren't younger than me you're an unc") 
    sleep(3)
else:
    print(f"Youngling why are you so young and why are you even using my code?")
    sleep(3)

if sport == "soccer":
    print(f"You are the goat w sport")
    sleep(3)
elif sport == "football":
    print(f"You are a bum")     
    sleep(3)
elif sport == "hockey":
    print(f"You use a stick to put a black disc in a goal what kinda sport is that")
    sleep(3)
elif sport == "baseball":
    print(f"I don't like you and your ice cream scoop hair")
    sleep(3)


if number != 67:
    print(f"Why is 67 not your favorite number you absolute freak")
    sleep(3)
else:
    print(f"I'm so happy your favorite number is 67 you are the goat")
    sleep(3)

if color == "purple":
    print(f"You are a pretty cool person")
elif color == "blue":
    print(f"Basic ah color")
elif color == "green":
    print(f"How do you even like that color")
elif color == "pink":
    print(f"Pink is a pretty cool color")
elif color == "red":
    print(f"Why do you like the color of blood weirdo")
sleep(3)

if candy == "kitcat":
    print(f"KitsKats seriosuly?")
elif candy == "hershey":
    print(f"Really thats your favorite candy you're an idiot for this being your favorite candy")
elif candy == "twix":
    print(f"That is some good taste in candy my friend")
elif candy == "100 grand":
    print(f"You are an unc")
elif candy == "skittles":
    print(f"You like to eat the rainbow?")
elif candy == "almond joy":
    print(f"You really like the eat almonds as a candy?")
sleep(3)