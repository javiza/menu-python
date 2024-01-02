# funcion agregar compra, parametro compras
def agregar_compra(compras):
    # pedimos al usuario que ingrese un monto de la compra que realizó
    monto = float(input("Ingrese el monto de la compra: "))
    # agregamos a compras
    compras.append(monto)
    # mensaje de vuelta
    print("Compra agregada correctamente.")

# funcion mostrar_compras, parametro compras
def mostrar_compras(compras):
    # si el largo de la variable compra es igual a 0, muestra no hay compras registradas
    if len(compras) == 0:
        print("No hay compras registradas.")
    # en caso que sea mayor a 0, lista de compras, con un ciclo for que enumera las compras y devuelve un espacio
    # end= "", imprime en la misma linea y no hace un salto de linea para concatenar
    else:
        print("Lista de compras:", end=" ")
        for i, compra in enumerate(compras):

            print(compra, end="")
            # en caso que la iteracion en i sea distinto al largo de la variable compras, menos 1, imprime lo que falta
            if i != len(compras) - 1:
                print(" -", end=" ")
        print()

# funcion mostrar_total, sumas las compras y concatenamos y con :.2f le damos el formato requerido
def mostrar_total(compras):
    total_gastado = sum(compras)
    print("Total gastado: ${:.2f}".format(total_gastado))

# funcion main
def main():
    # creamos la lista compras []
    compras = []
    # inicializada en 0
    total_gastado = 0
    # usamos el ciclo while para el menu para mostrar las opciones
    while True:
        print("\nMenú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")
        # aca se ingresa la opcion del usuario
        opcion = input("Seleccione una opción: ")
        # utilizamos if para la condicion, según la opcion que ingrese el usuario, las opciones del menú
        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("!Hasta luego¡")
            # utilizamos break para terminar el ciclo y que continue lo que sigue del codigo
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    main()
