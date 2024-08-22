import random
import math

lower_bond = int(input("Enter the lower bond : "))

upper_bond = int(input("Enter the upper bond : "))

computer = random.randint(lower_bond, upper_bond)    # generating random number between lower and upper bond.
total_chances = math.ceil(math.log(upper_bond - lower_bond + 1, 2))
print(f"You've only {total_chances} chance to guess")

for i in range(1, total_chances + 1):
    guess = int(input("Guess the number : "))

    if computer == guess:
        print(f"Congratulations you did it in {i} chance.")
        break 
    elif computer < guess:
        print(f"You guess too high")
    elif computer > guess:
        print(f"You guess too small")
else:
    print("You loose the game\nBetter luck next time")