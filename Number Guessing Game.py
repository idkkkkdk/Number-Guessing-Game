import random
number = random.randrange(1,11)

print ("Welcome to my number guessing game")
print ("You have to guess a number between 1 and 10")

while True:
    number_1 = int(input("Enter your guess or type 20 for a hint: "))
    if number_1 == 20:
        if number >= 5:
            print ("The number is bigger than 5!")
        else:
            print ("The number is less than 5")
    
    if number_1 == number:
        print ("Congrats you got the correct answer!")
        break
    elif number_1!=20:
        print("You got the wrong answer!")
        break
    


