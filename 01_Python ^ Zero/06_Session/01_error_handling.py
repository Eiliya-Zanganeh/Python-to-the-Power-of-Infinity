try:
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    result = num_1 / num_2

except ValueError as error: # (ValueError, ZeroDivisionError)
    print(f"Invalid input: {error}")
    # exit()

except ZeroDivisionError as error: # Exception as error
    print(f"Division by zero: {error}")
    # exit()

else:
    print(result)

finally:
    print("Program ended")






