import os
import datetime
import json
import random

# Variables
COLORS = {
    'black': "\033[30m",
    'red': "\033[31m",
    'green': "\033[32m",
    'yellow': "\033[33m",
    'blue': "\033[34m",
    'magenta': "\033[35m",
    'cyan': "\033[36m",
    'white': "\033[37m",
    'reset': "\033[0m",
}
DATA_PATH = 'data.json'
DATA = []


# Functions
def cprint(text, color='reset'):
    # Todo: If the provided color is not in the COLORS dictionary, default to 'reset'
    if ...:
        color = 'reset'

    print(f"{COLORS[color]}{text}{COLORS['reset']}")


def clear():
    # Todo: Research what this function does and how it clears the terminal screen
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")


def read_data():
    with open(DATA_PATH, "r", encoding="utf-8") as data_file:
        # Todo: Load JSON data from the file using json.load()
        loaded_data = ...

    for item in loaded_data:
        # Todo: Convert the start_datetime string to a datetime object using datetime.fromisoformat() (look up this method)
        item["start_datetime"] = ...
        # Todo: Convert the end_datetime string to a datetime object using datetime.fromisoformat()
        item["end_datetime"] = ...

    return loaded_data


def write_data():
    outputs = []

    for item in DATA:
        # Todo: Create a shallow copy of the current item to avoid modifying the original
        new_item = ...

        # Todo: Convert the start_datetime from a datetime object back to an ISO format string using .isoformat() (look up this method)
        new_item["start_datetime"] = ...
        # Todo: Convert the end_datetime from a datetime object back to an ISO format string using .isoformat()
        new_item["end_datetime"] = ...

        outputs.append(new_item)

    with open(DATA_PATH, "w", encoding="utf-8") as data_file:
        # Todo: Write the outputs list to the JSON file with indentation for readability and ensure_ascii=False to preserve non-ASCII characters
        ...


def get_movie_duration(item):
    # Todo: Calculate the time difference between end_datetime and start_datetime to get the movie duration
    duration = ...
    total_minutes = int(duration.total_seconds() // 60)

    # Todo: Calculate the number of whole hours by performing integer division on total_minutes
    hours = ...
    # Todo: Calculate the remaining minutes using the modulo operator on total_minutes
    minutes = ...

    # Todo: Return both hours and minutes as a tuple
    return


def show_time(*args):
    clear()
    # Todo: If no arguments are provided, display a custom message indicating no times are available
    if ...:
        cprint("No time found 😶‍🌫️", "yellow")

    # Todo: Iterate over the provided arguments using enumerate() to get both the index and the item
    for ... in ...:
        cprint(f"ID: {idx + 1}", "cyan")
        cprint(f"Movie: {item['movie']}", "cyan")
        cprint(f"Time: {item['start_datetime']} - {item['end_datetime']}", "cyan")
        cprint(f"Reservation: {item['reservation_count']}/{item['maximum_reservation']}", "cyan")
        hours, minutes = get_movie_duration(item)
        cprint(f"Movie duration: {hours}h {minutes}m", "cyan")
        cprint("-" * 20, 'white')


def add_new_time():
    clear()
    cprint("Add new time:")
    movie = input("Enter your title ( Tainatic Movie ): ")
    start_datetime = input("Enter your date ( 2026-05-08 10:30 ): ")
    end_datetime = input("Enter your date ( 2026-05-08 10:30 ): ")
    maximum_reservation = input("Enter your guest maximum reservation (5): ")

    # Todo: Parse the start and end datetime strings into datetime objects using datetime.strptime() with the format '%Y-%m-%d %H:%M'
    start_datetime = ...
    end_datetime = ...
    maximum_reservation = int(maximum_reservation)

    new_time = {
        'movie': movie,
        'start_datetime': start_datetime,
        'end_datetime': end_datetime,
        'maximum_reservation': maximum_reservation,
        'reservation_count': 0
    }
    # Todo: Append the new_time dictionary to the global DATA list
    ...

    write_data()
    clear()
    show_time(new_time)
    cprint("Time added ✅", "green")


def select_index():
    # Todo: Display all items in DATA by calling show_time() and unpacking the DATA list as arguments (use *DATA)
    ...


    if len(DATA) > 0:
        selected_index = int(input("Enter your choice ( ID ): ")) - 1
        # Todo: Validate that the selected_index is within the valid range (0 to len(DATA)-1)
        if ...:
            return selected_index
        else:
            clear()
            cprint("Invalid choice ❌", "red")
            cprint("-" * 20, 'white')
            return None
    else:
        return None


def remove_time():
    clear()
    selected_index = select_index()
    if selected_index is not None:
        # Todo: Remove the item at the selected_index from DATA using pop() and store the removed item for display
        removed_item = ...
        write_data()
        clear()
        show_time(removed_item)
        cprint(f"Time {selected_index + 1} removed ✅", "green")


def edit_time():
    clear()
    selected_index = select_index()
    if selected_index is not None:
        clear()
        movie = input("Enter your updated title ( Tainatic Movie ): ")
        start_datetime = input("Enter your updated date ( 2026-05-08 10:30 ): ")
        end_datetime = input("Enter your updated date ( 2026-05-08 10:30 ): ")
        maximum_reservation = input("Enter your updated guest maximum reservation (5): ")

        # Todo: Parse the updated start and end datetime strings into datetime objects using datetime.strptime() with the format '%Y-%m-%d %H:%M'
        start_datetime = ...
        end_datetime = ...
        maximum_reservation = int(maximum_reservation)

        updated_time = {
            'movie': movie,
            'start_datetime': start_datetime,
            'end_datetime': end_datetime,
            'maximum_reservation': maximum_reservation,
            'reservation_count': 0
        }
        # Todo: Replace the item at selected_index in DATA with the updated_time dictionary
        ...
        write_data()
        clear()
        show_time(updated_time)
        cprint(f"Time {selected_index + 1} updated ✅", "green")


def reserve_time():
    clear()
    selected_index = select_index()
    if selected_index is not None:
        clear()
        # Todo: Retrieve the current reservation_count and maximum_reservation values from DATA at the selected_index
        reservation_count = ...
        maximum_reservation = ...
        if reservation_count < maximum_reservation:
            # Todo: Increment the reservation_count for the item at selected_index in DATA by 1
            ...
            write_data()
            cprint(f"Reservation successfully! ({reservation_count + 1}/{maximum_reservation}) ✅", "green")
        else:
            cprint("Reservation limit exceeded! ❌", "red")


def get_available_times():
    # Todo: Use the filter() function with a lambda to return only those items from DATA where reservation_count is less than maximum_reservation
    return ...


def get_random_movie():
    clear()
    available_times = get_available_times()
    if len(available_times) > 0:
        # Todo: Use random.choice() to select a random movie from available_times and pass it to show_time()
        show_time(...)
    else:
        cprint("No time found 😶‍🌫️", "yellow")


def search_movie():
    clear()
    search_param = input("Enter your movie title: ").lower()
    for item in DATA:
        if search_param in item['movie'].lower():
            show_time(item)
            # Todo: Stop the loop once the first matching movie is found
            ...
        else:
            # Todo: Skip to the next iteration of the loop
            ...

    # Todo: Understand when the else clause of a for loop executes (it runs only if the loop completes without hitting a break)
    else:
        cprint("No movie found 😶‍🌫️", "yellow")


def show_movies():
    clear()

    # Todo: Replace this loop with a list comprehension that extracts the 'movie' field from each item in DATA
    outputs = []
    for item in DATA:
        outputs.append(item['movie'])

    # Todo: Replace this loop with the map() function to truncate each movie title to the first 10 characters
    outputs = []
    for item in outputs:
        outputs.append(item[:10])

    # Todo: Remove duplicate movie titles by converting the list to a set, then back to a list
    outputs = ...

    # Todo: Loop through outputs using enumerate() to display each movie with its index
    for ... in ...:
        cprint(f"{idx + 1} - {item}", "cyan")


def main():
    # Todo: Understand why the global keyword is used here (it allows modification of the DATA variable defined outside the function)
    global DATA

    clear()
    DATA = read_data()

    cprint("Welcome to Cinema Reservation System 👋", "cyan")

    while True:
        cprint("1 - Show all times", "magenta")
        cprint("2 - Add new time", "magenta")
        cprint("3 - Update time", "magenta")
        cprint("4 - Delete time", "magenta")
        cprint("5 - Reservation time", "magenta")
        cprint("6 - Show available times", "magenta")
        cprint("7 - Search movie", "magenta")
        cprint("8 - Show movies ( not times )", "magenta")

        user_choice = input("Enter your choice (1 - 4) or q to quit: ").lower()

        if user_choice == '1':
            # Todo: Call show_time() and pass all items from DATA by unpacking the list (use *DATA)
            ...

        elif user_choice == '2':
            add_new_time()

        elif user_choice == '3':
            edit_time()

        elif user_choice == '4':
            remove_time()

        elif user_choice == '5':
            reserve_time()

        elif user_choice == '6':
            clear()
            available_times = get_available_times()
            # Todo: Display the available times by calling show_time() and unpacking the available_times list (use *available_times)
            ...

        elif user_choice == '7':
            search_movie()

        elif user_choice == '8':
            show_movies()

        else:
            # Todo: Exit the while loop (and the program) when the user enters 'q' or an invalid choice
            ...


main()