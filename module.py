
# Funcion Obtener bumeranes

def BoomerangFunction(my_list):
    my_couter = 0
    i = 0
    while i < len(my_list)-1:
        try:
            if my_list[i] == my_list[i+2]: #IndexError: list index out of range
                my_couter += 1
                print("Boomerang")
            else:
                print("No es Boomerang")

        except IndexError:
            print("No es Boomerang")
            
        i += 1

    print(f"El numero total de Boomerangs del array es {my_couter}")
