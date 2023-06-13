global_variable = "Global"

def variable_print(arg):
    local_variable = "Local"
    print(global_variable)
    print(local_variable)
    print(arg)

parameter = input()
variable_print(parameter)
