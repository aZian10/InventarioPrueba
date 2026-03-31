def agregar_producto(nombre, precio, cantidad):
    #Pide el nombre del producto al usuario
    nombre=str(input("Ingrese un nombre: "))
    #Veficar que los datos correspondan
    while True:
        try:
            precio=float(input("Ingrese el precio: "))
            if precio<=0:
                raise ValueError
            break
        except ValueError:
            print("Ingrese un dato valido")
    while True:
        try:
            cantidad=int(input("Ingrese cantidad: "))
            if cantidad<=0:
                raise ValueError
            break
        except ValueError:
            print("Ingrese un dato valido")
        #Guardamos el total
        costo_total=precio*cantidad
        #Muestra el resultado en consola
    return nombre, precio, cantidad 

def mostrar_inventario():
    print("-----------------------------------")
    print(f"Nombre: {nombre}\n Precio: {precio}\n Cantidad: {cantidad}\n Costo total: {costo_total}")
    print("-----------------------------------")
    return

def calcular_estadisticas():
    return

    