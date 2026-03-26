import csv

def save_csv(inventory, path, include_header=True):
    """Guarda el inventario en CSV con manejo de errores."""
    if not inventory:
        print("No se puede guardar. Inventario vacio.")
        return
    
    try:
        # Abre el archivo en modo escritura ('w')
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
            if include_header:
                writer.writeheader() # Escribe la primera fila de encabezados
            writer.writerows(inventory) # Escribe todos los datos del diccionario
        print(f"Inventario guardado en: {path}")
    except (PermissionError, IOError) as e:
        print(f"Error de escritura: {e}")

def load_csv(path):
    """Carga y valida datos de CSV. Retorna (lista, contador_errores)."""
    loaded_products = []
    invalid_rows = 0
    
    if not path.lower().endswith('.csv'):
        print("Error: Solo se admiten archivos con extensión .csv")
        return None, 0
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None) # Lee y salta la fila del encabezado
            
            # Verifica si el encabezado coincide con los requisitos
            if header != ["name", "price", "quantity"]:
                print("Formato CSV invalido.")
                return None, 0

            for row in reader:
                try:
                    # Valida longitud de fila y tipos de datos
                    if len(row) != 3: raise ValueError
                    name = row[0].strip()
                    price = float(row[1])
                    quantity = int(row[2])
                    # Asegura que no haya numeros negativos
                    if price < 0 or quantity < 0: raise ValueError
                    loaded_products.append({"name": name, "price": price, "quantity": quantity})
                except (ValueError, IndexError):
                    invalid_rows += 1 # Cuenta filas que fallaron la validacion
                    
        return loaded_products, invalid_rows
    except FileNotFoundError:
        print("Archivo no encontrado.")
    except Exception as e:
        print(f"Error inesperado: {e}")