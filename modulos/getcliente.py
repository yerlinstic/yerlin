from tabulate import tabulate
import storage.cliente as cli

def getAllClientName():
    clienteName = list()
    for val in cli.clientes:
        codigoName = dict({
            "codigo": val.get('codigo_cliente'),
            "nombre": val.get('nombre_cliente')
        })
        clienteName.append(codigoName)
    return clienteName

def getOneClientCodigo(codigo):
    for val in cli.clientes:
        if(val.get('codigo_cliente') == codigo):
            return [{
                "codigo": val.get('codigo_cliente'),
                "nombre": val.get('nombre_cliente')
            }]

def getAllClientCreditCiudad(limiteCredit, ciudad):
    clienteCredic = list()
    for val in cli.clientes:
        if(val.get('limite_credito') >= limiteCredit and val.get('ciudad') == ciudad):
            clienteCredic.append({
                "Codigo": val.get('codigo_cliente'),
                "Responsable": val.get('nombre_cliente'),
                "Director": f"{val.get('nombre_contacto')} {val.get('nombre_contacto')}",
                "Telefono": val.get('telefono'),
                "Fax": val.get('fax'),
                "Direcciones": f"{val.get('linea_direccion1')} {val.get('linea_direccion2')}",
                "Origen": f"{val.get('pais')} {val.get('region')} {val.get('ciudad')} {val.get('codigo_postal')}",
                "Codigo del asesor": val.get('codigo_empleado_rep_ventas'),
                "Credito": val.get('limite_credito')
            })
    return clienteCredic

def menu():
    while True:
        print(""" 
    ____                        __                   __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
          /_/                                                                                                   

            0. Regresar al menu principal
            1. Obtener todos los clientes (codigo y nombre)
            2. Obtener un cliente por el codigo 
            3. Obtener toda la informacoin de un cliente segun su limite de credito y ciudad que pertenece (ejem: 1500.0, Fuenlabrada )
          
          """)        
        opcion = int(input("\nSelecione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
        elif(opcion == 2):
            codigoCliente = int(input("Ingrese el codigo del cliente: "))
            print(tabulate(getOneClientCodigo(codigoCliente), headers="keys", tablefmt="github"))
        elif(opcion == 3):
            limite = float(input("Ingrese el limite de credito de los clientes que deseas vizualizar: "))
            ciudad = input("Ingrese el nombre de la ciudad que deseas filtrar los clientes: ")
            print(tabulate(getAllClientCreditCiudad(limite, ciudad), headers="keys", tablefmt="github"))
        elif(opcion == 0):
            break















