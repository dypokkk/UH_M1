def add_product(inventory, name, price, quantity):
    """Agrega un nuevo diccionario de producto a la lista de inventario."""
    # Añade un nuevo diccionario con los datos proporcionados
    inventory.append({
        "name": name,
        "price": float(price),
        "quantity": int(quantity)
    })
    print(f"Producto '{name}' agregado exitosamente.")

def show_inventory(inventory):
    """Muestra el inventario en un formato de tabla limpio."""
    if not inventory:
        print("El inventario esta vacio.")
        return
    
    # Imprime el encabezado de la tabla con espaciado especifico
    print(f"\n{'Nombre':<20} | {'Precio':<10} | {'Cantidad':<10}")
    print("-" * 45)
    for p in inventory:
        # Imprime cada fila con formato de 2 decimales para el precio
        print(f"{p['name']:<20} | ${p['price']:>9.2f} | {p['quantity']:>10}")

def search_product(inventory, name):
    """Retorna el diccionario del producto si se encuentra, de lo contrario None."""
    for p in inventory:
        # Comparacion insensible a mayusculas
        if p["name"].lower() == name.lower():
            return p
    return None

def update_product(inventory, name, new_price=None, new_quantity=None):
    """Actualiza los valores de un producto existente."""
    p = search_product(inventory, name)
    if p:
        # Solo actualiza si se proporciono un valor (no es None)
        if new_price is not None: p["price"] = float(new_price)
        if new_quantity is not None: p["quantity"] = int(new_quantity)
        print(f"Producto '{name}' actualizado.")
        return True
    return False

def delete_product(inventory, name):
    """Elimina un producto de la lista."""
    p = search_product(inventory, name)
    if p:
        inventory.remove(p) # Elimina el objeto diccionario especifico
        print(f"Producto '{name}' eliminado.")
        return True
    return False

def calculate_statistics(inventory):
    """Calcula metricas del inventario usando lambdas."""
    if not inventory:
        return None
    
    # Task 3: Lambda para calcular el subtotal (precio * cantidad)
    get_subtotal = lambda p: p["price"] * p["quantity"]
    
    # Suma totales usando expresiones generadoras
    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(get_subtotal(p) for p in inventory)
    
    # Task 3: Encuentra valores maximos usando lambdas como clave de comparacion
    most_expensive = max(inventory, key=lambda p: p["price"])
    highest_stock = max(inventory, key=lambda p: p["quantity"])
    
    return {
        "total_units": total_units,
        "total_value": total_value,
        "expensive_name": most_expensive["name"],
        "expensive_price": most_expensive["price"],
        "stock_name": highest_stock["name"],
        "stock_qty": highest_stock["quantity"]
    }