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

    
# def nada_main():
#     # Define the party (Hospital in this case)
#     hospital = Party(name="Hospital")
    
#     # Secret inputs for patient's hospitalization data
#     total_days_in_hospital = SecretInteger(Input(name="total_days_in_hospital", party=hospital))
#     days_in_ICU = SecretInteger(Input(name="days_in_ICU", party=hospital))
#     total_medical_expenses = SecretInteger(Input(name="total_medical_expenses", party=hospital))

#     # Perform basic arithmetic operations
#     average_cost_per_day = total_medical_expenses / total_days_in_hospital
#     ratio_of_ICU_days = days_in_ICU / total_days_in_hospital

#     # Output the results to the hospital
#     return [
#         Output(average_cost_per_day, "average_cost_per_day", hospital),
#         Output(ratio_of_ICU_days, "ratio_of_ICU_days", hospital),
#     ]
