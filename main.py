import os
import modules.getGamas as gG

def clear_screen():
    os.system("clear")

def show_main_menu():
    clear_screen()
    print(""" 
                                                            
                                                                                                                                               
            _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
            (_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_)
                                                                                                                                                                                                                                                                     
            ____  _                            _     __               __   __  ___                    ____       _            _             __
           / __ )(_)__  ____ _   _____  ____  (_)___/ /___     ____ _/ /  /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
          / __  / / _ \/ __ \ | / / _ \/ __ \/ / __  / __ \   / __ `/ /  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
         / /_/ / /  __/ / / / |/ /  __/ / / / / /_/ / /_/ /  / /_/ / /  / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
        /_____/_/\___/_/ /_/|___/\___/_/ /_/_/\__,_/\____/   \__,_/_/  /_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                                                                            /_/                

          
          
                    
                                                                    1. Cliente
                                                                    2. Oficina
                                                                    3. Empleado
                                                                    4. Pedidos
                                                                    5. Productos
                                                                    6. Gamas de Productos
                                                                    0. Salir
                                                                                                                                               
            _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
            (_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_)
                                                                                                                                                
                                                                                                                                     
                                                                                                                                     
     
          
          
          
          
          
          """)

def main_menu():
    while True:
        show_main_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
           
            pass
        elif opcion == "2":
            
            pass
        elif opcion == "3":
          
            pass
        elif opcion == "4":
           
            pass
        elif opcion == "5":
            menu_producto()
        elif opcion == "6":
            menu_gamas()
        elif opcion == "0":
            break

def menu_producto():
    pass

def menu_gamas():
    while True:
        clear_screen()

        print("""

                                                                                                                                                                                

                                             _  __   _  __   _  __   _  __   _  __   _  __   _  __   _  __   _  __                                 
                                            | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/                                 
                                            _>  <   _>  <   _>  <   _>  <   _>  <   _>  <   _>  <   _>  <   _>  <                                            
                                            /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|                                                                              

                                                        ____  _                                _     __    
                                                       / __ )(_)__  ____ ___ _   _____  ____  (_)___/ /___ 
                                                      / __  / / _ \/ __ `__ \ | / / _ \/ __ \/ / __  / __ \
                                                     / /_/ / /  __/ / / / / / |/ /  __/ / / / / /_/ / /_/ /
                                                    /_____/_/\___/_/ /_/ /_/|___/\___/_/ /_/_/\__,_/\____/ 
                                                                                                                                                        
                                                                    1. Mostrar todas las gamas
                                                                    2. Mostrar una gama por ID
                                                                    3. Crear una nueva gama
                                                                    4. Actualizar una gama existente
                                                                    5. Eliminar una gama
                                                                    0. Regresar al menú principal
                                                                                                                                     
                                             _  __   _  __   _  __   _  __   _  __   _  __   _  __   _  __   _  __                                 
                                            | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/  | |/_/                                 
                                            _>  <   _>  <   _>  <   _>  <   _>  <   _>  <   _>  <   _>  <   _>  <                                            
                                            /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|  /_/|_|                                                                              
             
              
              """)


opcion = input("\nSeleccione una opción: ")
solicitud = input("Ingrese la opcion a la que quiera acceder: ")

        if solicitud == "1":
        os.system("clear")
        Empleados.menu()
        break
        elif solicitud == "2":
        os.system("clear")
        Pago.menu()
        break
        elif solicitud == "3":
        os.system("clear")
        Oficinas.menu()
        break
        elif solicitud == "4":
        os.system("clear")
        Clientes.menu()
        break
        elif solicitud == "5":
        os.system("clear")
        Producto.menu()
        break
        elif solicitud == "6":
        os.system("clear")
        Pedido.menu()
        break
        elif solicitud.upper() == "X":
        exit()
        else:
        print("Esta opcion no es valida")
        input("Presione enter para continuar")


def show_all_gamas():
    clear_screen()
    print("=== Todas las Gamas ===")
    gamas = gG.get_all_gamas()
    for gama in gamas:
        print(gama)
    input("Presione Enter para continuar...")

def show_gama_by_id():
    clear_screen()
    print("=== Mostrar Gama por ID ===")
    gama_id = input("Ingrese el ID de la gama: ")
    gama = gG.get_gama_by_id(gama_id)
    if gama:
        print(gama)
    else:
        print("Gama no encontrada.")
    input("Presione Enter para continuar...")

def create_new_gama():
    clear_screen()
    print("=== Crear Nueva Gama code --list-extensions | xargs -L 1 code --uninstall-extension ===")
    gama_info = {
        "name": input("Ingrese el nombre de la nueva gama: "),
        "description": input("Ingrese la descripción de la nueva gama: ")
    }
    new_gama_id = gG.create_gama(gama_info)
    if new_gama_id:
        print("Nueva gama creada con ID:", new_gama_id)
    else:
        print("Error al crear la nueva gama.")
    input("Presione Enter para continuar...")

def update_existing_gama():
    clear_screen()
    print("=== Actualizar Gama Existente ===")
    gama_id = input("Ingrese el ID de la gama a actualizar: ")
    new_gama_info = {
        "name": input("Ingrese el nuevo nombre de la gama: "),
        "description": input("Ingrese la nueva descripción de la gama: ")
    } 
    if gG.update_gama(gama_id, new_gama_info):
        print("Gama actualizada correctamente.")
    else:
        print("Error al actualizar la gama.")
    input("Presione Enter para continuar...")

    def delete_gama():
        clear_screen()
        print("=== Eliminar Gama ===")
        gama_id = input("Ingrese el ID de la gama a eliminar: ")
        if gG.delete_gama(gama_id):
            print("Gama eliminada correctamente.")
        else:
            print("Error al eliminar la gama.")
        input("Presione Enter para continuar...")

    if __name__ == "__main__":
        main_menu()
