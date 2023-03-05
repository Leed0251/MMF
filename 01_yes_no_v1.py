# functions go here

# main routine goes here

while True:
    show_instructions = input("Do you want to read the instructions? ").lower()

    if show_instructions == "yes" or show_instructions == "y":
        print("Intructions go here")
    elif show_instructions == "no" or show_instructions == "n":
        pass
    else:
        print("Please answer yes / no")

print("We are done")