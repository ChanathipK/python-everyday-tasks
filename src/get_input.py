def get_string_input() -> str:
    user_input = ""
    is_input_valid = False
    while not is_input_valid:
        try:
            user_input = input("input: ").strip()
            if user_input != "":
                is_input_valid = True
        except Exception:
            print("invalid input, try again.")
            
    return user_input