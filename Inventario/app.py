import servicios
import archivos

def menu():
    print("\n" + "="*30)
    print("  GESTIÓN DE INVENTARIO (CSV)")
    print("="*30)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    return input("Seleccione una opción (1-9): ")

def solicitar_num(mensaje, tipo=float):
    """Valida que la entrada sea numérica y no negativa."""
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor < 0:
                print("❌ No se permiten valores negativos.")
                continue
            return valor
        except ValueError:
            print(f"❌ Entrada inválida. Debe ser un número ({tipo.__name__}).")

def main():
    inventario = []
    
    while True:
        opcion = menu()

        if opcion == "1":
            nombre = input("Nombre del producto: ").strip()
            precio = solicitar_num("Precio: ", float)
            cantidad = solicitar_num("Cantidad: ", int)
            servicios.agregar_producto(inventario, nombre, precio, cantidad)
            print("✅ Producto agregado.")

        elif opcion == "2":
            servicios.mostrar_inventario(inventario)

        elif opcion == "3":
            nombre = input("Nombre a buscar: ")
            prod = servicios.buscar_producto(inventario, nombre)
            if prod:
                print(f"🔍 Encontrado: {prod}")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ")
            print("(Deje vacío para no cambiar)")
            p_input = input("Nuevo precio: ")
            c_input = input("Nueva cantidad: ")
            
            nuevo_p = float(p_input) if p_input else None
            nueva_c = int(c_input) if c_input else None
            
            if servicios.actualizar_producto(inventario, nombre, nuevo_p, nueva_c):
                print("✅ Producto actualizado.")
            else:
                print("❌ No se encontró el producto.")

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ")
            if servicios.eliminar_producto(inventario, nombre):
                print("🗑️ Producto eliminado.")
            else:
                print("❌ No se encontró el producto.")

        elif opcion == "6":
            stats = servicios.calcular_estadisticas(inventario)
            if stats:
                print("\n--- ESTADÍSTICAS ---")
                print(f"📦 Unidades totales: {stats['unidades']}")
                print(f"💰 Valor total: ${stats['valor']:.2f}")
                print(f"💎 Más caro: {stats['mas_caro']['nombre']} (${stats['mas_caro']['precio']})")
                print(f"📈 Mayor stock: {stats['mayor_stock']['nombre']} ({stats['mayor_stock']['cantidad']} und)")
            else:
                print("⚠️ Inventario vacío.")

        elif opcion == "7":
            ruta = input("Nombre del archivo para guardar (ej: datos.csv): ")
            archivos.guardar_csv(inventario, ruta)

        elif opcion == "8":
            ruta = input("Nombre del archivo a cargar: ")
            nuevos_datos, errores = archivos.cargar_csv(ruta)
            
            if nuevos_datos is not None:
                op = input("¿Sobrescribir inventario actual? (S/N): ").upper()
                if op == "S":
                    inventario[:] = nuevos_datos
                    accion = "Reemplazo"
                else:
                    # Fusión: si existe actualiza precio y suma cantidad, si no, agrega
                    for n in nuevos_datos:
                        existente = servicios.buscar_producto(inventario, n['nombre'])
                        if existente:
                            existente['precio'] = n['precio']
                            existente['cantidad'] += n['cantidad']
                        else:
                            inventario.append(n)
                    accion = "Fusión"
                
                print(f"\n✅ Proceso terminado ({accion})")
                print(f"📊 Cargados: {len(nuevos_datos)} | Omitidos por error: {errores}")

        elif opcion == "9":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()



