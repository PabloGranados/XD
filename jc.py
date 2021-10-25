print("Bienvenido a los salu2. Escribe (salir) para finalizar el programa")
print("Este programa es hecho por mi:)")


def saludos():
    nombre = ""
    while nombre != "salir":
        nombre = input("Ingrese su nombre: ")
        if nombre == "salir":
            break
        elif nombre == "Juan Carlos":
            print("Hola, " + nombre+", ¿Cómo estas chupapijas?")
        else:
            print("¿Cómo estas, "+nombre+"?")


saludos()
