"""Checks if number is even or odd."""
def get_integer_input():
    """Gets an integer from user."""
    number = int(input("Enter a integer: "))
    return number

def check_even_odd(num_value):
    """Checks if number even or odd."""
    if num_value % 2 == 0:
        message = f"{num_value} is an Even number."
    else:
        message = f"{num_value} is an Odd number."
    return message

if __name__ == "__main__":
    num = get_integer_input()
    RESULT = check_even_odd(num)
    print(RESULT)
