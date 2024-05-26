def get_positive_int_input() -> int:
    is_input_valid = False
    user_input = ""
    while not is_input_valid:
        try:
            user_input = int(input("n: "))
            if user_input <= 0:
                print("n has to be greater than 0, try again.")
            else:
                is_input_valid = True
        except Exception as e:
            print("invalid input:", e)
    return user_input


def fibonacci():
    n = get_positive_int_input()
    pass
