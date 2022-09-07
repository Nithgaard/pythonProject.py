# This is a Python Project for teaching clean code concepts

class Employee:
    def __init__(self, age, years_employed, is_retired):
        self.age = age
        self.years_employed = years_employed
        self.is_retired = is_retired


# Magic Number exercise
def is_legal_drinking_age_dirty(age):
    if age > 21:
        return True
    else:
        return False


# Solution to Magic Number exercise
# Use consts to describe the numbers you are using to your programs.
def is_legal_drinking_age_clean(age):
    # Write your clean version here
    return 0  # remove this to run your version


# Be positive exersise
def is_logged_in_dirty(is_not_logged_in):
    if is_not_logged_in == True:
        print("Succesfully logged in.")
        return True
    else:
        print("Failed to logged in.")
        return False


# Solution to Be positive exersise
def is_logged_in_clean(is_not_logged_in):
    # Write your clean version here
    return 0  # remove this to run your version


# Intermediate exercise
# What is the question answering?
def eligible_for_pension_dirty(employee):
    if employee.age > 55 and employee.years_employed > 10 and employee.is_retired:
        return True
    else:
        return False


# Solution to ohm Intermediate exercise
# An intermediate Variable says a lot more them a long expression
def eligible_for_pension_clean(employee):
    # Write your clean version here
    return 0  # remove this to run your version


# Ternary exersise
def get_price_dirty(is_preordered):
    if is_preordered == True:
        return 200
    else:
        return 350


# Solution to Ternary exersise
# Use a oneline Ternary.
def get_price_clean(is_preordered):
    # Write your clean version here
    return 0  # remove this to run your version


if __name__ == "__main__":
    # Call methods here to check if they work
    print(is_legal_drinking_age_dirty(22) == is_legal_drinking_age_clean(22))
    print(is_logged_in_dirty(True) == is_logged_in_clean(True))
    print(eligible_for_pension_dirty(Employee(55, 13, True)) == eligible_for_pension_clean(Employee(55, 13, True)))
    print(get_price_dirty(True) == get_price_clean(True))
