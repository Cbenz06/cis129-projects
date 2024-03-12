#Caleb Benzi
#March 8th, 2024
#Calculates the payout by bottles recieved

# Step 1: Declare variables below 
totalBottles = 0
totalPayout = 0
todayBottles = 0
counter = 1
keepGoing = "y"
NBR_OF_DAYS = 8
PAYOUT_PER_BOTTLE = .1
# Step 2: Loop to run program again
while counter <= NBR_OF_DAYS:
    todayBottles = int(input('Input number of bottles returned for day #' + str(counter) + ' '))
    totalBottles += todayBottles
    counter += 1

    if counter == NBR_OF_DAYS:
        totalPayout = totalBottles * PAYOUT_PER_BOTTLE
        print('The total number of bottles collected is', totalBottles)
        print('The total paid out is $' + str(totalPayout))
        print('Do you want to enter another week\'s worth of data?\n(y or n)')
        keepGoing = input()

        if keepGoing == 'y':
            totalPayout = 0
            totalBottles = 0
            counter = 1
            continue
        else:
            break

