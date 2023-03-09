import pandas
import random
from datetime import date

# functions go here


# Shows instructions
def show_instructions():
    print("""
***** Instructions *****

For each ticket, enter ...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will also be automatically written to
a text file.

*************************
    """)


# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter a whole number")


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # ticket is $7.50 for users under 16
    if var_age < 16:
        return 7.5

    # ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        return 10.5

    # ticket price is $6.5 for seniors (65+)
    else:
        return 6.5


# checks that users enter a valid response (e.g. yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])
    
    while True:

        response = input(question).lower()

        for valid in valid_responses:
            if response == valid[:num_letters] or response == valid:
                return valid

        print(error)


def currency(x):
    return "${:.2f}".format(x)


# main routine starts here

# set maximum number of tickets below
maxTickets = 5
ticketsSold = 0

yesNoList = ["yes", "no"]
paymentList = ["cash", "credit"]

# Lists to hold ticket details
allNames = []
allTicketCosts = []
allSurcharge = []

# Dictionary used to create data frame ie: column_name:list
miniMovieDict = {
    "Name": allNames,
    "Ticket Price": allTicketCosts,
    "Surcharge": allSurcharge
}

# Ask user if they want to see the instructions
displayInstructions = string_checker("Do you want to read the instructions (y/n): ", 1, yesNoList)

if displayInstructions == "yes":
    show_instructions()

print()

# loop to sell tickets
while ticketsSold < maxTickets:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name.lower() == "xxx" and len(allNames) > 0:
        break
    elif name.lower() == "xxx":
        print("You must sell at least ONE ticket before quitting")
        continue

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Sorry you are too young for this movie")
        continue
    else:
        print("?? That looks like a typo, please try again.")
        continue

    # Calculate ticket cost
    ticketCost = calc_ticket_price(age)

    # get payment method
    payMethod = string_checker("Choose a payment method (cash / credit): ", 2, paymentList)

    if payMethod == "cash":
        surcharge = 0
    else:
        # Calculate 5% surcharge if users are paying by credit card
        surcharge = ticketCost * 0.05

    ticketsSold += 1

    # Add ticket name, cost and surcharge to lists
    allNames.append(name)
    allTicketCosts.append(ticketCost)
    allSurcharge.append(surcharge)

# Create data frame from dictionary to organise information
miniMovieFrame = pandas.DataFrame(miniMovieDict)
# mini_movie_frame = mini_movie_frame.set_index("Name")

# Calculate the total ticket cost (ticket + surcharge)
miniMovieFrame["Total"] = miniMovieFrame["Surcharge"] + miniMovieFrame["Ticket Price"]

# Calculate the profit for each ticket
miniMovieFrame["Profit"] = miniMovieFrame["Ticket Price"] - 5

# Calculate ticket and profit totals
total = miniMovieFrame["Total"].sum()
profit = miniMovieFrame["Profit"].sum()

# choose a winner and look up total won
winnerName = random.choice(allNames)
winIndex = allNames.index(winnerName)
totalWon = miniMovieFrame.at[winIndex, "Total"]

# Currency Formatting (uses currency function)
addDollars = ["Ticket Price", "Surcharge", "Total", "Profit"]
for varItem in addDollars:
    miniMovieFrame[varItem] = miniMovieFrame[varItem].apply(currency)

# set index at end (before printing)
miniMovieFrame = miniMovieFrame.set_index("Name")

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "---- Mini Movie Fundraiser Ticket Data ({}/{}/{})".format(day, month, year)
filename = "MMF_{}_{}_{}".format(year, month, day)

# Change frame to a string so that we can export it to file
miniMovieString = pandas.DataFrame.to_string(miniMovieFrame)

# Create strings for printing...
ticketCostHeading = "\n----- Ticket Cost / Profit -----"
totalTicketSales = "Total Ticket Sales: ${}".format(total)
totalProfit = "Total Profit : ${}".format(profit)

# Edit text below!! It needs to work if we have unsold tickets
salesStatus = "\n*** All the tickets have been sold ***"

winnerHeading = "\n---- Raffle Winner ----"
winnerText = "The winner of the raffle is {}. "\
    "They have won ${}. ie: Their ticket is " \
    "free!".format(winnerName, totalWon)

# list holding content to print / write to file
toWrite = [heading, miniMovieString, ticketCostHeading,
           totalTicketSales, totalProfit, salesStatus,
           winnerHeading, winnerText]

# Print output
for item in toWrite:
    print(item)

# Write output to file
# Create file to hold date (add .txt extension)
writeTo = "{}.txt".format(filename)
textFile = open(writeTo, "w+")

for item in toWrite:
    textFile.write(item)
    textFile.write("\n")

textFile.close()

print()
# Output number of tickets sold
if ticketsSold == maxTickets:
    print("\nCongratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(
        ticketsSold, maxTickets - ticketsSold
    ))
