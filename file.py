def enter_number(message):
    number = input(message)
    try:
        float(number)

    except ValueError:
        print("Please enter the number, try again!")
        return enter_number(message)
    return number


def enter_list():
    user_list = input("Enter your list, separate by space:\n>").split()
    return user_list