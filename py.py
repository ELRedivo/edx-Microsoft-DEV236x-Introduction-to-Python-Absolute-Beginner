# [ ] review the code, run, fix the error

tickets = int(input("Enter tickets remaining (0 to quit): "))

#################### WHILE #######################################
while tickets != 0:
    
    # if tickets are multiple of 3 then "winner"
    if int(tickets/3) == tickets/3:
        print("You win!")
        break
    else:
        print("Sorry, not a winner.")
    
    tickets = int(input("Enter tickets remaining (0 to quit): "))
##################################################################

print("Game ended.")
