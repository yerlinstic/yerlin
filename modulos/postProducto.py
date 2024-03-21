import os
import json
import requests


def postProducto():
    producto = {
        "codigo_producto": input("Ingrese el código del producto: "),
        "nombre": input("Ingrese el nombre del producto: "),
        "gama": input("Ingrese la gama del producto: "),
        "dimensiones": input("Ingrese las dimensiones del producto: "),
        "proveedor": input("Ingrese el proveedor del producto: "),
        "descripcion": input("Ingrese la descripción del producto: "),
        "cantidad_en_stock": int(input("Ingrese la cantidad en stock del producto: ")),
        "precio_venta": float(input("Ingrese el precio de venta del producto: ")),
        "precio_proveedor": float(input("Ingrese el precio del proveedor del producto: "))
    }
    
    url = "http://172.16.102.108:5501/productos"  
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(producto))
        response.raise_for_status()
        res = response.json()
        res["Mensaje"] = "Producto Guardado"
        return [res]
    except requests.exceptions.RequestException as e:
        return [{"Error": f"Error al enviar la solicitud: {e}"}]


def deleteProducto(id_producto):
   
    pass

def menu():
    while True:
        os.system("clear")
        print("""  
                                                                    
                                                                              
    ___       __          _       _      __                         __      __                    __ 
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__      
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \     
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/     
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/      
    ____  ____  ____  ____  __  __________________  _____                                                   
   / __ \/ __ \/ __ \/ __ \/ / / / ____/_  __/ __ \/ ___/                                                   
  / /_/ / /_/ / / / / / / / / / / /     / / / / / /\__ \                                                    
 / ____/ _, _/ /_/ / /_/ / /_/ / /___  / / / /_/ /___/ /                                                    
/_/   /_/ |_|\____/_____/\____/\____/ /_/  \____//____/                                                     
                   
                    
                    1. Guardar un producto nuevo
                    2. Eliminar un producto
                    0. Atrás
                    """)        
                           
  
opcion = input("\nSeleccione una de las opciones: ")
if opcion == "1":
            print(postProducto())
            input("Presione una tecla para continuar.....")
elif opcion == "2":
            id_producto = input("\nIngrese el ID del producto que desea eliminar: ")
            deleteProducto(id_producto)
            input("Presione una tecla para continuar.....")
elif opcion == "0":
    break


def main():
    menu()

if __name__ == "__main__":
    main()
