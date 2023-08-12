import os
from art import logo


# Function to clear the console screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to conduct the auction
def auction(name, bid):
    # Dictionary to store bidders and their bids
    bidders = {}

    # Initialize the maximum bid and last user status
    max_bid = 0
    isLastUser = False

    # Loop until the last user indicates they're done
    while not isLastUser:
        # Add the current bidder's name and bid to the dictionary
        bidders[name] = bid

        # Ask if the current user is the last user
        lastUser = input("Are you the last user? 'yes' or 'no': ").lower()

        if lastUser == "yes" or lastUser == "y":
            clear()  # Clear the console output
            isLastUser = True  # Set the loop termination flag
        else:
            clear()  # Clear the console output
            name = input("Welcome to the secret auction program.\nWhat is your name?: ")
            bid = int(input("What is your bid?: $"))

    # Find the highest bidder
    for user in bidders:
        if bidders[user] > max_bid:
            max_bid = bidders[user]
            max_bidder = user

    # Print the highest bidder's information
    print(logo)
    print(f"The maximum bidder is {max_bidder} and the bid was ${max_bid}")


# Get user's name and initial bid
print(logo)
name = input("Welcome to the secret auction program.\nWhat is your name?: ")
bid = int(input("What is your bid?: $"))

# Call the auction function with user's input
auction(name, bid)
