coins = 0
print("You have {} coins.".format(coins))
more = input("Do you want another? yes or no ")
while more == "yes":
    coins += 1
    print("You have {} coins.".format(coins))
    more = input("Do you want another? yes or no ")
print("Bye")
