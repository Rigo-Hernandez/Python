# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
# print ("goodbye")

try: 
    number = int(input("Enter a number: "))
    result = number/0
except ValueError:
    print("enter a number: ")
except ZeroDivisionError:
    print("Cant divide by zero: ")
except:
    print("Something bad happend: ")
finally:
    print("closing statement")