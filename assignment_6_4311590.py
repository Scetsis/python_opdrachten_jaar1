def user_input() -> int:
    number_input = int(input("Choose a number. The numbers 0 and 10 are valid numbers."))
    if number_input < 0 or number_input > 10:
        raise ValueError('{number_input} is not between 0 and 10.'.format(number_input = number_input))
    else:
        return number_input

def two_correct_user_values():
    print("Please enter two numbers between 0 and 10.")
    valid_numbers = []
    while len(valid_numbers) < 2:
        try:
            valid_number = user_input()
            valid_numbers.append(valid_number)
        except ValueError as in_case_of_error:
            print(in_case_of_error.args[0])
            print("The number you chose does comply to the given ruleset, please try again.")
    return valid_numbers

def divide_user_input():
    valid_numbers = two_correct_user_values()
    try:
        return valid_numbers[0] / valid_numbers[1]
    except ZeroDivisionError:
        return None




if __name__ == "__main__":
    hutsefluts = divide_user_input()
    print(hutsefluts)