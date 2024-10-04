try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1) when will a ValueError occur?
# when the user input invalid number. for example: * entering float number when the user input asking for integer input
#                                                  * entering string data when the user input asking for integer input
#                                                  * entering no value(empty)
#                                                  * entering anything except integer(whole number)
# 2) when will a ZeroDivision occur?
# In python any number divided by zero will show ZeroDivisionError

# 3) could you change the code to avoid the possibility of a ZeroDivisionError?
# yes I can with error checking.

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator"))
    while denominator == 0:
        print("Cant divided by Zero")
        denominator = int(input("Enter the denominator: "))
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")