from time import sleep

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
    if n == 1 or n == 2:
        print("fibonacci at n: 1")
    else:
        q1 = 1
        q2 = 1
        temp = 0
        for i in range(n - 2):
            temp = q1 + q2
            q1 = q2
            q2 = temp
        print(f"fibonacci at n: {temp}")
    sleep(1)
    print("Count down from ")
    sleep(1)
    for i in range(5):
        print(5 - i, "...", sep="")
        sleep(1)
