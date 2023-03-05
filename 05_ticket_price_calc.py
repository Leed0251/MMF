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


# loop for testing...
while True:

    # Get age (assume users input a valid integer)
    age = int(input("Age: "))

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket Price: ${:.2f}".format(age, ticket_cost))