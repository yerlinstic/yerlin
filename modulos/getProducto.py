import os
from tabulate import tabulate
import requests


def getAllData():
   
    peticion = requests.get("http://172.16.102.108:5501")
    data = peticion.json()
    return data

def getAllStocksPriceGama(gama, stock):
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("cantidad_en_stock") >= stock):
            condiciones.append(val)
    def price(val):
        return val.get("precio_venta")    
    condiciones.sort(key=price, reverse=True)
    for i, val in enumerate(condiciones):
        condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta": val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama": val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "proveedor": val.get("proveedor"),
                "descripcion": f'{val.get("descripcion")[:5]}...' if condiciones[i].get("descripcion") else None,
                "stock": val.get("cantidad_en_stock"),
                "base": val.get("precio_proveedor")
            }
    return condiciones

def menu():
    while True:
        os.system("clear")
        print("""  
    ____                        __                   __                             __           __            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                             /_/                                                  

            1. Obtener todos los productos de una categoría ordenando sus precio de venta, también que su cantidad de inventario sea superior (ejem: Ornamentales, 100 )
            0. Atras
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            gama = input("Ingrese la gama que deseas flictrar: ")
            stock = int(input("Ingrese las unidades que seas mostrar: "))
            print(tabulate(getAllStocksPriceGama(gama, stock), headers="keys", tablefmt="github"))
        elif(opcion == 0):
            break