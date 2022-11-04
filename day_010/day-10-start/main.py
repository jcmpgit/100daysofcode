#Functions with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    #print(f"{formated_f_name} {formated_l_name}")
    return f"{formated_f_name} {formated_l_name}"


print(format_name("John", "DoE"))

#Functions with Outputs mulitpe returns

def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide vaild inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"


print(format_name(input("What is your first name? "), input("What is your last name? ")))