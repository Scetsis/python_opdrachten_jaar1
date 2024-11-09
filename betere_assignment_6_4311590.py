def number_input() -> int:
    inputted_number = int(input("Submit a number between 0 and 10 where 0 and 10 are included: "))
    if inputted_number < 0 or inputted_number > 10:
        raise ValueError ("{x} is not between 0 and 10.".format(x=inputted_number))
    return inputted_number

def two_correct_user_values() -> []:
    numbers = []
    print("Submit 2 valid numbers between 0 and 10. So that we can divide them:")
    read_error = 0
    while len(numbers) < 2:
        try:
            number = number_input()
            # if len(numbers) == 1 and number == 0:
            #     print("Division by zero is not possible.")
            # else:
            #     numbers.append(number)
            numbers.append(number)
        except ValueError as error:
            read_error = read_error + 1
            print(error.args[0])
            if read_error < 3:
                print("Good job reading.")
            if read_error >= 3:
                print("Are you fucking stupid?????")
            if read_error > 5:
                print("How dumb can you be??")
    return numbers

def divide_user_input():
    numbers = two_correct_user_values()
    try:
        divided_numbers = numbers[0] / numbers[1]
        return divided_numbers
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    hoi = divide_user_input()
    print(hoi)