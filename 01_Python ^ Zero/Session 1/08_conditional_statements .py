age = input("Enter your age: ")

if age:
    age = int(age)

    if age >= 18:
        print("Ok")
    else:
        print("NOK")

else:
    print("invalid input")


# password = input("Enter your password: ")

# if password == 'admin admin':
#     print("Welcome admin ...")

# elif password == '123':
#     print("Welcome staff ...")

# elif password == '1234':
#     print("Welcome user ...")

# else:
#     print("Invalid password")