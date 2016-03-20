
#
# inventory.py:
#
#   Implements a simple inventory tracking program using
#       dictionaries.

# testing git stuff...

def getCommand():
    command = input("Enter command: ")
    return command

def addToInventory(dict):
    pass

def viewInventory(dict):
    pass

def main():

    print ("Welcome to StuffMaster.")

    inventory = {} # empty dictionary

    while True: # get command, process command

        result = getCommand()

        if result == 'A':
            addToInventory(inventory)
        elif result == 'V':
            viewInventory(inventory)
        elif result == 'Q':
            break
        else:
            print ("Invalid command: try again.")

    # here, we're quitting: print out final version of inventory

    print ("Quitting. Final version of inventory is:")

    # what else should we do here?

    print ("Exiting...")

main()
