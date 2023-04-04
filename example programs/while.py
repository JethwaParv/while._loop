# CST08: Compulsory Task 3


# Assigned variable
# Total is the sum of numbers the user has entered.
# counter counts the number of times the user enters numbers.
total = 0
user_input = 0
counter = 0
average = 0


# While True statement ensures that the loop the continues until the condition has changed.
# While True is also used as we don't know how many inputs are needed.
# if statement with comparison operators.
while True:
    user_input = int(input('Please enter a number or -1 to exit: '))
    if user_input != -1:             # != is for not equal to.
        counter += 1                 # The counter counts the every time the user inputs a number
        print('The counter value: {}'.format(counter))
        total += user_input          # Each time the user enters a number the previous total is added to that new value.
        print('The total value: {}'.format(total))


# The break statement ensures the while loop breaks once the above condition is achieved.
    else:
        break


# The print statement outside the while as its only applied once if statement is achieved.
average = total/counter
print('The average of the numbers entered: {} '.format(average))





