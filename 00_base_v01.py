# functions go here

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

# checks that users enter a vlid response (eg yes / no
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0],valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2
    
    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# main routine starts here

# set maximum number of tickets below
max_tickets = 3
tickets_sold = 0

yes_no_list = ["yes","no"]
payment_list = ["cash","credit"]

# Ask user if they want to see the instructions
display_instructions = string_checker("Do you want to read the instructions (y/n): ",
1,yes_no_list)

if display_instructions == "yes":
    print("Instructions go here")

print()

# loop to sell tickets
while tickets_sold < max_tickets:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == "xxx":
        break

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
    ticket_cost = calc_ticket_price(age)

    # get payment method
    pay_method = string_checker("Choose a payment method (cash / credit): ",2,payment_list)
    
    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets")
else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining".format(
        tickets_sold, max_tickets - tickets_sold
    ))
