BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"


def custom_print(text, color="blue"):
    if color == 'black':
        print(f"{BLACK}{text}")
    elif color == 'red':
        print(f"{RED}{text}")
    elif color == 'green':
        print(f"{GREEN}{text}")
    elif color == 'yellow':
        print(f"{YELLOW}{text}")
    elif color == 'blue':
        print(f"{BLUE}{text}")
    elif color == 'magenta':
        print(f"{MAGENTA}{text}")
    elif color == 'cyan':
        print(f"{CYAN}{text}")
    elif color == 'white':
        print(f"{WHITE}{text}")

    print(RESET, end='')


custom_print(text="Hello World")
custom_print(text="Hello World", color="yellow")
