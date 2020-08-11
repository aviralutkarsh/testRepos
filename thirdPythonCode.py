#The third file with Python ccode. Let's write a simple function to check if a number is even or not.
def checkNum(number):
    if (number > 0 and (number % 2)==0):
        val = "The entered integer is even!"
    elif (number == 0):
        val = "The entered integer is zero which is neither even nor odd!"
    elif (number < 0):
        val = "Please enter positive integers only!"
    else:
        val = "The entered integer is odd!"
    return val

checkNum(45)
checkNum(0)
checkNum(78)
checkNum(-56)
