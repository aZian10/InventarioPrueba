import csv

def guardar_csv(inventario, ruta):
    """Guarda la lista de diccionarios en un archivo CSV."""
    if not inventario:
        print("⚠️ Error: No hay datos para guardar.")
        return
    
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            campos = ["nombre", "precio", "cantidad"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(inventario)
        print(f"✅ Inventario guardado en: {ruta}")
    except Exception as e:
        print(f"❌ Error al guardar: {e}")

def cargar_csv(ruta):
    """Lee un CSV y valida fila por fila. Retorna (lista_productos, num_errores)."""
    productos_cargados = []
    errores = 0
    try:
        with open(ruta, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            # Validar encabezado mínimo
            if not reader.fieldnames or not all(c in reader.fieldnames for c in ["nombre", "precio", "cantidad"]):
                print("❌ Formato de encabezado inválido.")
                return None, 0

            for fila in reader:
                try:
                    # Validar que existan los datos y sean correctos
                    nombre = fila['nombre'].strip()
                    precio = float(fila['precio'])
                    cantidad = int(fila['cantidad'])
                    
                    if precio < 0 or cantidad < 0:
                        raise ValueError
                        
                    productos_cargados.append({
                        "nombre": nombre, 
                        "precio": precio, 
                        "cantidad": cantidad
                    })
                except (ValueError, KeyError, TypeError):
                    errores += 1
        return productos_cargados, errores
    except FileNotFoundError:
        print("❌ Archivo no encontrado.")
        return None, 0
    except Exception as e:
        print(f"❌ Error crítico: {e}")
        return None, 0

