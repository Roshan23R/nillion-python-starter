from nada_dsl import *

def nada_main():
    party1 = Party(name="Party1")
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Perform basic arithmetic operations
    addition_result = my_int1 + my_int2
    subtraction_result = my_int1 - my_int2
    multiplication_result = my_int1 * my_int2
    division_result = my_int1 / my_int2

    # Output the results of the computations
    return [
        Output(addition_result, "addition_result", party1),
        Output(subtraction_result, "subtraction_result", party1),
        Output(multiplication_result, "multiplication_result", party1),
        Output(division_result, "division_result", party1),
    ]