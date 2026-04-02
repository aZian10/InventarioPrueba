def agregar_producto(inventario, nombre, precio, cantidad):
    producto={"nombre": nombre, "precio":float(precio), "cantidad": int(cantidad)}
    inventario.append(producto)

def mostrar_inventario(inventario):
    if not inventario:
        print("Inventario vacio")
        return
    print("Inventario actual")
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: {p['precio']:.2f} | Cantidad: {p['cantidad']}")

def buscar_producto(inventario, nombre):
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    p=buscar_producto(inventario,nombre)
    if p:
        if nuevo_precio is not None: p["precio"]= nuevo_precio
        if nueva_cantidad is not None: p["cantidad"]= nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    p=buscar_producto(inventario,nombre)
    if p:
        inventario.remove(p)
        return True
    return False

def calcular_estadisticas(inventario):
    if not inventario:
        return None
    
    subtotal= lambda p: p["precio"] * p["cantidad"]

    unidades_totales=sum(p["cantidad"] for p in inventario)
    valor_total=sum(subtotal(p) for p in inventario)
    p_mas_caro=max(inventario, key=lambda p: p["precio"])
    c_mayor=max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades": unidades_totales,
        "valor": valor_total,
        "mas_caro": p_mas_caro,
        "cantidad_mayor": c_mayor
    }

