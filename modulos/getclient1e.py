from tabulate import tabulate
import storage.cliente as cli

def obtener_nombres_clientes():
    nombres_clientes = []
    for cliente in cli.clientes:
        nombre_cliente = {
            "codigo": cliente.get('codigo_cliente'),
            "nombre": cliente.get('nombre_cliente')
        }
        nombres_clientes.append(nombre_cliente)
    return nombres_clientes

def obtener_cliente_por_codigo(codigo):
    for cliente in cli.clientes:
        if cliente.get('codigo_cliente') == codigo:
            return [{
                "codigo": cliente.get('codigo_cliente'),
                "nombre": cliente.get('nombre_cliente')
            }]

def obtener_clientes_por_limite_credito_y_ciudad(limite_credito, ciudad):
    clientes_filtrados = []
    for cliente in cli.clientes:
        if cliente.get('limite_credito') >= limite_credito and cliente.get('ciudad') == ciudad:
            clientes_filtrados.append({
                "Codigo": cliente.get('codigo_cliente'),
                "Responsable": cliente.get('nombre_cliente'),
                "Director": f"{cliente.get('nombre_contacto')} {cliente.get('nombre_contacto')}",
                "Telefono": cliente.get('telefono'),
                "Fax": cliente.get('fax'),
                "Direcciones": f"{cliente.get('linea_direccion1')} {cliente.get('linea_direccion2')}",
                "Origen": f"{cliente.get('pais')} {cliente.get('region')} {cliente.get('ciudad')} {cliente.get('codigo_postal')}",
                "Codigo del asesor": cliente.get('codigo_empleado_rep_ventas'),
                "Credito": cliente.get('limite_credito')
            })
    return clientes_filtrados

def menu():
    while True:
        print(""" 
        ██████╗ ██████╗ ██╗  ██╗███████╗██████╗      █████╗ ███████╗ █████╗ ██╗  ██╗
        ██╔══██╗██╔══██╗██║ ██╔╝██╔════╝██╔══██╗    ██╔══██╗╚══███╔╝██╔══██╗╚██╗██╔╝
        ██████╔╝██████╔╝█████╔╝ █████╗  ██████╔╝    ███████║  ███╔╝ ███████║ ╚███╔╝ 
        ██╔═══╝ ██╔══██╗██╔═██╗ ██╔══╝  ██╔══██╗    ██╔══██║ ███╔╝  ██╔══██║ ██╔██╗ 
        ██║     ██║  ██║██║  ██╗███████╗██║  ██║    ██║  ██║███████╗██║  ██║██╔╝ ██╗
        ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝

            0. Regresar al menú principal
            1. Obtener todos los clientes (código y nombre)
            2. Obtener un cliente por el código 
            3. Obtener toda la información de un cliente según su límite de crédito y ciudad que pertenece (ejem: 1500.0, Fuenlabrada)
          """)        
        opcion = int(input("\nSeleccione una de las opciones: "))
        if opcion == 1:
            print(tabulate(obtener_nombres_clientes(), headers="keys", tablefmt="github"))
        elif opcion == 2:
            codigo_cliente = int(input("Ingrese el código del cliente: "))
            print(tabulate(obtener_cliente_por_codigo(codigo_cliente), headers="keys", tablefmt="github"))
        elif opcion == 3:
            limite = float(input("Ingrese el límite de crédito de los clientes que desea visualizar: "))
            ciudad = input("Ingrese el nombre de la ciudad que desea filtrar los clientes: ")
            print(tabulate(obtener_clientes_por_limite_credito_y_ciudad(limite, ciudad), headers="keys", tablefmt="github"))
        elif opcion == 0:
            break

menu()
