
import os

if not os.path.exists("datos.txt"):
    with open("datos.txt", "w") as file:
        pass
def readline(filepath="datos.txt"):
    with open(filepath, "r") as file:
        read = file.readlines()
    return read


def appen(item, filepath="datos.txt"):
    with open(filepath, "a") as file:
        appenda= file.write(item + "\n")
        return appenda


def write(argumento, filepath="datos.txt"):
    with open(filepath, "w") as file:
        file.writelines(argumento)


def show(nota):
    for index, item in enumerate(nota):
        print(f"{index + 1}-{item}")


def edit(value, poder):
    seleccion = value['lista'][0]
    nueva_palabra = value['information']

    index = poder.index(seleccion)
    poder[index] = nueva_palabra + "\n"
    return poder

