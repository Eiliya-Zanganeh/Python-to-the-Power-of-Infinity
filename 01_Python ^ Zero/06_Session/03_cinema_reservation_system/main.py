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
    if color not in COLORS.keys():
        color = 'reset'
    print(f"{COLORS[color]}{text}{COLORS['reset']}")


def clear():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux / macOS
        os.system("clear")


def read_data():
    with open(DATA_PATH, "r", encoding="utf-8") as data_file:
        loaded_data = json.load(data_file)

    for item in loaded_data:
        item["start_datetime"] = datetime.datetime.fromisoformat(item["start_datetime"])
        item["end_datetime"] = datetime.datetime.fromisoformat(item["end_datetime"])

    return loaded_data


def write_data():
    outputs = []

    for item in DATA:
        new_item = item.copy()

        new_item["start_datetime"] = new_item["start_datetime"].isoformat()
        new_item["end_datetime"] = new_item["end_datetime"].isoformat()

        outputs.append(new_item)

    with open(DATA_PATH, "w", encoding="utf-8") as data_file:
        json.dump(outputs, data_file, indent=4, ensure_ascii=False)


def get_movie_duration(item):
    duration = item["end_datetime"] - item["start_datetime"]
    total_minutes = int(duration.total_seconds() // 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return hours, minutes


def show_time(*args):
    clear()
    if len(args) == 0:
        cprint("No time found 😶‍🌫️", "yellow")

    for idx, item in enumerate(args):
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

    start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
    end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M')
    maximum_reservation = int(maximum_reservation)

    new_time = {
        'movie': movie,
        'start_datetime': start_datetime,
        'end_datetime': end_datetime,
        'maximum_reservation': maximum_reservation,
        'reservation_count': 0
    }
    DATA.append(new_time)
    write_data()
    clear()
    show_time(new_time)
    cprint("Time added ✅", "green")


def select_index():
    show_time(*DATA)
    if len(DATA) > 0:
        selected_index = int(input("Enter your choice ( ID ): ")) - 1
        if 0 <= selected_index < len(DATA):
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
        removed_item = DATA.pop(selected_index)
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

        start_datetime = datetime.datetime.strptime(start_datetime, '%Y-%m-%d %H:%M')
        end_datetime = datetime.datetime.strptime(end_datetime, '%Y-%m-%d %H:%M')
        maximum_reservation = int(maximum_reservation)

        updated_time = {
            'movie': movie,
            'start_datetime': start_datetime,
            'end_datetime': end_datetime,
            'maximum_reservation': maximum_reservation,
            'reservation_count': 0
        }
        DATA[selected_index] = updated_time
        write_data()
        clear()
        show_time(updated_time)
        cprint(f"Time {selected_index + 1} updated ✅", "green")


def reserve_time():
    clear()
    selected_index = select_index()
    if selected_index is not None:
        clear()
        reservation_count = DATA[selected_index]['reservation_count']
        maximum_reservation = DATA[selected_index]['maximum_reservation']
        if reservation_count < maximum_reservation:
            DATA[selected_index]['reservation_count'] += 1
            write_data()
            cprint(f"Reservation successfully! ({reservation_count + 1}/{maximum_reservation}) ✅", "green")
        else:
            cprint("Reservation limit exceeded! ❌", "red")


def get_available_times():
    return list(filter(lambda x: x['reservation_count'] < x['maximum_reservation'], DATA))


def get_random_movie():
    clear()
    available_times = get_available_times()
    if len(available_times) > 0:
        show_time(random.choice(available_times))
    else:
        cprint("No time found 😶‍🌫️", "yellow")


def search_movie():
    clear()
    search_param = input("Enter your movie title: ").lower()
    for item in DATA:
        if search_param in item['movie'].lower():
            show_time(item)
            break
        else:
            continue
    else:
        cprint("No movie found 😶‍🌫️", "yellow")


def show_movies():
    clear()

    outputs = [item['movie'][:10] for item in DATA]
    # outputs = list(map(lambda x:x['movie'][:10], outputs))

    outputs = set(outputs)

    for idx, item in enumerate(outputs):
        cprint(f"{idx + 1} - {item}", "cyan")


def main():
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
            show_time(*DATA)

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
            show_time(*available_times)

        elif user_choice == '7':
            search_movie()

        elif user_choice == '8':
            show_movies()

        else:
            break


if __name__ == '__main__':
    main()
