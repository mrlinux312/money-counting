print("Money Counting Game")
print("Rules: Enter a number for each coin that will add up to a dollar to win the game")

quarters = float(input("Enter number of quarters:")) * .25
dimes = float(input("Enter number of dimes:")) * .10
nickels = float(input("Enter number of nickels:")) * .05
pennies = float(input("Enter number of pennies:")) * .01

total = quarters + dimes + nickels + pennies

if total > 1.00:
    print("The total was more than a dollar")
elif total == 1.00:
   print(f"Congratulations you win the game! Your total is ${total:.2f}")
elif total < 1.00:
   print("The Total was less than a dollar")