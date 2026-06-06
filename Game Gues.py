import random 
number = random.randint(1 , 100)

attempts = 0

while True:
    guess = int(input("Gues karo (1,100):"))
    attempts = attempts +1

    if guess < number:
        print("number chota! Bara guess karo")
    elif guess > number:
        print("Number bara! Chota guess karo")
    else:
        print("Shabash sahi guess kiya!")
        print("Total attempts", attempts)
        break

