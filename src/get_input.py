def get_string_input(allowed_input: list[str]) -> str:
    user_input = ""
    is_input_valid = False
    while not is_input_valid:
        try:
            user_input = input("input: ").strip()
            if user_input != "" and user_input.lower() in allowed_input:
                is_input_valid = True
        except Exception:
            print("invalid input, try again.")
        if not is_input_valid:
            print("given input doesn't match any choice, try again.")
    
    return user_input