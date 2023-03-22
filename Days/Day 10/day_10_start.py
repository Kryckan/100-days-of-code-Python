def format_name(f_name: str, l_name: str):
    if f_name == "" or l_name == "":
        return "Input error. Please try again"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


print(
    format_name(
        input("What is your first name? \n"), input("What is your last name? \n")
    )
)
