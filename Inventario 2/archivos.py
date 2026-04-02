import csv

def guardar_csv(inventario,ruta):
    if not inventario:
        print("No hay datos")
        return
    
    try:
        with open(ruta, 'w', newline='', encoding='utf-8') as f:
            campos=["nombre", "precio", "cantidad"]
            writer=csv.DictWriter(f,fieldnames=campos)
            writer.writeheader()
            writer.writerow(inventario)
        print("Inventario guardado en: {ruta}")
    
    except Exception as e:
        print("Error al guardar: {e}")

def cargar_csv(ruta):
    productos_cargados=[]
    errores=0
    try:
        with open(ruta,'r', encoding='utf-8') as f:   
            reader=csv.DictReader(f)
            if not reader.fieldnames or not all(c in reader.fieldnames for c in ["nombre","precio","cantidad"]):
                print("Cabezado invalido")
                return None, 0
            
            for fila in reader:
                try:
                    nombre=fila['nombre'].strip()
                    precio=float(fila['precio'])
                    cantidad=int(fila['cantidad'])

                    if precio<0 or cantidad<0:
                        raise ValueError
                    
                    productos_cargados.append({
                        "nombre":nombre,
                        "precio":precio,
                        "cantidad":cantidad
                    })
                except (ValueError,KeyError,TypeError):
                    errores+=1
        return productos_cargados, errores
    except FileNotFoundError:
        print("Archivo no encontrado")
        return None,0
    except Exception as e:
        print(f"Error critico {e}")
        return None, 0 