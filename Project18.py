import random
count=random.randint(1,100)
#print(count)

Tries=0
guess=-50
while guess != count:
    guess=int (input("Mantepse"))
    Tries = Tries +1




    if guess > count:
        print("Kateva")
    elif guess < count:
        print("Aneva")
    else:
        print("Bravo")

if guess==count:
    print("You won")

else:
    print("You lost")