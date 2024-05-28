import sys

sys.path.append("./src/")
sys.path.append("./src/maths/")
sys.path.append("./src/gui/")

from get_input import get_string_input
from second_degree_polynomial import solve_equation as solve_2nd_polynomial
from fibonacci import fibonacci
from unit_conversion import tk_main as unit_conversion

programs = [["solve 2nd degrees polynomial equation", solve_2nd_polynomial], ["convert units using a GUI app", unit_conversion], ["get nth element from a fibonacci sequence", fibonacci]]

print("Welcome to the EverydayTasksProgram!")
print(f"There are currently {len(programs)} programs you can use.")

for i in range(len(programs)):
    print(f"type {i+1}:\t{programs[i][0]}")

allowed_inputs = [str(e+1) for e in range(len(programs))]
allowed_inputs.append("q")
user_input = get_string_input(allowed_input=allowed_inputs);

while user_input != "q":
    print("")
    programs[int(user_input) - 1][1]()
    print("")
    for i in range(len(programs)):
        print(f"type {i+1}:\t{programs[i][0]}")
    
    user_input = get_string_input(allowed_input=allowed_inputs);

print("thank you for using our programs.")