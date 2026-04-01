def agregar_producto(inventario, nombre, precio, cantidad):
    """Agrega un nuevo producto como diccionario a la lista."""
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)

def mostrar_inventario(inventario):
    """Imprime el inventario en formato de tabla simple."""
    if not inventario:
        print("⚠️ El inventario está vacío.")
        return
    print("\n--- INVENTARIO ACTUAL ---")
    for p in inventario:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Stock: {p['cantidad']}")

def buscar_producto(inventario, nombre):
    """Retorna el diccionario del producto o None si no existe."""
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """Actualiza precio y/o cantidad de un producto existente."""
    p = buscar_producto(inventario, nombre)
    if p:
        if nuevo_precio is not None: p["precio"] = nuevo_precio
        if nueva_cantidad is not None: p["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """Elimina un producto por nombre."""
    p = buscar_producto(inventario, nombre)
    if p:
        inventario.remove(p)
        return True
    return False

def calcular_estadisticas(inventario):
    """Calcula métricas clave usando lambdas y comprensiones."""
    if not inventario:
        return None

    subtotal = lambda p: p["precio"] * p["cantidad"]
    
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    p_mas_caro = max(inventario, key=lambda p: p["precio"])
    p_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    return {
        "unidades": unidades_totales,
        "valor": valor_total,
        "mas_caro": p_mas_caro,
        "mayor_stock": p_mayor_stock
    }
