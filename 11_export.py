import pandas
import random
from datetime import date

# lists to hold ticket details
allNames = ["a", "b", "c", "d", "e"]
allTicketCosts = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

miniMovieDict = {
    "Name": allNames,
    "Ticket Price": allTicketCosts,
    "Surcharge": surcharge
}
# create frame
miniMovieFrame = pandas.DataFrame(miniMovieDict)

# Calculate the total ticket cost (ticket + surcharge)
miniMovieFrame["Total"] = miniMovieFrame["Surcharge"] \
    + miniMovieFrame["Ticket Price"]

# Calculate the profit for each ticket
miniMovieFrame["Profit"] = miniMovieFrame["Ticket Price"] - 5

# Calculate ticket and profit totals
total = miniMovieFrame["Total"].sum()
profit = miniMovieFrame["Profit"].sum()

# Choose winner and look up total won
winnerName = random.choice(allNames)
winIndex = allNames.index(winnerName)
totalWon = miniMovieFrame.at[winIndex, "Total"]

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

# Close file
textFile.close()
