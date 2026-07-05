import datetime

def get_year(birthdate):
    now = datetime.datetime.now()
    birthdate = datetime.datetime.strptime(birthdate, '%Y-%m-%d')
    diff = (now - birthdate).days
    diff /= 365.25
    diff = round(diff)
    print(f"{diff} years old")


user_input = input("Please enter your birthdate: ")
get_year(user_input)