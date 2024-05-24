def solve_equation():
    is_input_valid = False
    a, b, c = 0, 0, 0
    while not is_input_valid:
        try:
            print("type in the equation in this form: Ax^2 + Bx + C = 0")
            equation = input("equation: ").split(" ")
            if len(equation) == 7:
                if equation[-1] != "0":
                    raise Exception("the equation must be in the correct form.")
                str_a = equation[0][0:-3:1]
                str_b = equation[2][0:-1:1]
                str_c = equation[4]
                a = float(str_a)
                b = float(str_b)
                c = float(str_c)
                is_input_valid = True
                return solve(a, b, c)
            elif len(equation) == 5:
                pass
            elif len(equation) == 3:
                pass
            else:
                raise Exception
        except Exception as e:
            message = f"invalid input: {e}"
            print(e)


def solve(a, b, c):
    x1 = (0-b + (b**2 - 4*a*c) ** (1/2))/(2*a)
    x2 = (0-b - (b**2 - 4*a*c) ** (1/2))/(2*a)
    result1 = 0
    result2 = 0
    if type(x1) == complex:
        real = round(x1.real, 2)
        imag = round(x1.imag, 2)
        result1 = complex(real=real, imag=imag)
    else:
        result1 = round(x1, 2)
    if type(x2) == complex:
        real = round(x2.real, 2)
        imag = round(x2.imag, 2)
        result2 = complex(real=real, imag=imag)
    else:
        result2 = round(x2, 2)
    print("=" * len(str([result1, result2])))
    return [result1, result2]

