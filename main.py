from functions import *
from files import *

def main():
    inventory = [] # Almacenamiento en memoria (lista de dicts)
    option_select = 0 # Variable de control para el bucle

    while option_select != 9:
        print("\n" + "="*35)
        print("   SISTEMA DE GESTION DE INVENTARIO")
        print("="*35)
        print(f"1. Add Product\n2. Show All\n3. Search\n4. Update\n5. Delete\n6. Statistics\n7. Save to CSV\n8. Load from CSV\n9. Exit")
        
        try:
            # Captura de la opcion del usuario
            option_select = int(input("Seleccione una opcion (1-9): "))
            
            if option_select == 1:
                name = input("Nombre del producto: ")
                price = float(input("Precio: "))
                qty = int(input("Cantidad: "))
                if price < 0 or qty < 0: raise ValueError("No se permiten valores negativos.")
                add_product(inventory, name, price, qty)

            elif option_select == 2:
                show_inventory(inventory)

            elif option_select == 3:
                name = input("Buscar por nombre: ")
                res = search_product(inventory, name)
                print(f"Encontrado: {res}" if res else "No encontrado.")

            elif option_select == 4:
                name = input("Nombre del producto a actualizar: ")
                p_in = input("Nuevo precio (Enter para omitir): ")
                q_in = input("Nueva cantidad (Enter para omitir): ")
                update_product(inventory, name, 
                               float(p_in) if p_in else None, 
                               int(q_in) if q_in else None)

            elif option_select == 5:
                name = input("Nombre del producto a eliminar: ")
                delete_product(inventory, name)

            elif option_select == 6:
                s = calculate_statistics(inventory)
                if s:
                    print(f"\nESTADISTICAS:\n- Unidades Totales: {s['total_units']}\n- Valor Total: ${s['total_value']:,.2f}")
                    print(f"- Mas Caro: {s['expensive_name']} (${s['expensive_price']})")
                    print(f"- Mayor Stock: {s['stock_name']} ({s['stock_qty']} unidades)")
                else:
                    print("Inventario vacio.")

            elif option_select == 7:
                path = input("Nombre del archivo para guardar (ej: datos.csv): ")
                save_csv(inventory, path)

            elif option_select == 8:
                path = input("Nombre del archivo a cargar: ")
                new_data, errors = load_csv(path)
                if new_data is not None:
                    print(f"Items hallados: {len(new_data)}. Errores: {errors}")
                    mode = input("¿Sobrescribir inventario actual? (S/N): ").upper()
                    if mode == 'S':
                        inventory[:] = new_data
                        print("Inventario reemplazado.")
                    else:
                        for item in new_data:
                            exist = search_product(inventory, item["name"])
                            if exist:
                                exist["quantity"] += item["quantity"]
                                exist["price"] = item["price"]
                            else:
                                inventory.append(item)
                        print("Inventario fusionado.")

            elif option_select == 9:
                print("Saliendo del programa exitosamente.")
            
            elif option_select > 9 or option_select < 1:
                print("Por favor, ingrese un numero valido entre 1 y 9.")

        except ValueError as e:
            # Captura errores si el usuario no ingresa un numero o ingresa negativos
            print(f"Error de entrada: Asegurese de usar numeros validos. ({e})")
        except Exception as e:
            # Captura cualquier otro error para que el programa no se cierre
            print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()