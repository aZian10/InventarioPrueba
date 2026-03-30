#Lista para guardar inventario
inventario=[]

def agregar_producto():
    #Veficar que los datos correspondan
    try:
        nombre=input("Ingrese un nombre: ")
        precio=float(input("Ingrese el precio: "))
        cantidad=int(input("Ingrese cantidad: "))
        producto={"nombre":nombre, "precio":precio, "cantidad":cantidad}
        inventario.append(producto)

    except ValueError:
        print("Ingrese datos validos")

def mostrar_inventario():
    if not inventario:
        print("El inventario esta vacio")
    else:
        print("Inventario")
        for i in inventario:
            print(f"Producto: {i['nombre']} | Precio: {i['precio']:.2f} | Cantidad: {i['cantidad']}")

def calcular_estadisticas():
    print("Estadisticas")
    if not inventario:
        print("No hay datos")
        return
    
    valor_total=sum(i['precio']* i['cantidad'] for i in inventario)
    total_unidades=sum(i['cantidad'] for i in inventario)

    print(f"Valor total: {valor_total:.2f}")
    print(f"Cantidad total: {total_unidades}")

def menu():
    while True:
        print("Sistema de gestion")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Calcular estadisticas")
        print("4. Salir")

        opcion=input("Seleccione una opcion:")

        if opcion=="1":
            agregar_producto()
        elif opcion=="2":
            mostrar_inventario()
        elif opcion=="3":
            calcular_estadisticas()
        elif opcion=="4":
            print("Salir")
            break
        else:
            print("Opcion invalida")

if __name__=="__main__":
    menu()

    