
from tabulate import tabulate
import modules.getClients as clientes
import modules.getEmpleados as empleados
import modules.getOficinas as oficinas
import modules.getPago as pago
import modules.getPedido as pedido
import modules.getProducto as producto

print("#1") 
print(tabulate(oficinas.getoficinasciu(),headers=["codigo_oficina","Ciudad"],tablefmt="grid"))

print("#2")
print(tabulate(oficinas.getCiudadTelefonoEspaña(),headers=["ciudad","telefono"],tablefmt="grid"))

print("#3")
print(tabulate(empleados.getempleadosboss(7),headers=["Nombre","Apellido 1","Apellido 2","Email","Codigo Jefe"],tablefmt="grid"))

print("#4")
print(tabulate(empleados.getboss(),headers=["Puesto","Nombre","Apellido 1","Apellido 2","Email"],tablefmt="grid"))

print("#5")
print(tabulate(empleados.getrepresentanteVentasEmp(),headers=["Nombre","Apellido 1","Apellido 2","Puesto"],tablefmt="grid"))

print("#6")
print(tabulate(clientes.getClienteEspaña(),headers=["Nombre Clientes Españoles"],tablefmt="grid"))

print("#7")
print(tabulate(pedido.getEstadoPedid(),headers=["Estados"],tablefmt="grid"))

print("#8")
print(tabulate(pago.getpay(),headers=["codigo_cliente"],tablefmt="grid"))

print("#9")
print(tabulate(pedido.getPedidoTarde(),headers=["Codigo Pedido","Codigo Cliente","Fecha Esperada","Fecha Entrega","Dias de Retrazo"],tablefmt="grid"))

print("#10")
print(tabulate(pedido.getPedido2DiasTarde(),headers=["Codigo Pedido","Codigo Cliente","Fecha Esperada","Fecha Entrega","Dias de Retrazo"],tablefmt="grid"))

print("#11")
print(tabulate(pedido.getEstadoPedid(),headers=["Codigo Pedido","Comentario"],tablefmt="grid"))

print("#12")
print(tabulate(pedido.getpedidosDeEnero(),headers=["Codigo Pedido","Fecha Esperada","Fecha entrega","Comentario"],tablefmt="grid"))

print("#13")
print(tabulate(pago.getPayPaypal2008(),headers=["Forma Pago","Fecha Pedido","Total"],tablefmt="grid"))

print("#14")
print(tabulate(pago.getformasPago(),headers=["Forma Pago"],tablefmt="grid"))

print("#15")
print(tabulate(producto.getornamentales(),headers=["Codigo Producto","Gama","Cantidada En Stock"],tablefmt="grid"))

print("#16")
print(tabulate(clientes.getClientesMadrid(),headers=["Codigo Cliente","Nombre Cliente","Pais","Region","Codigo Empleado","Nombre Empleado","Puesto"],tablefmt="grid"))

print("#17")
print(tabulate(clientes.getRepresentanteClientes(),headers=["Codigo Cliente","Nombre Cliente","Codigo Empleado","Nombre Empleado","Apellidos"],tablefmt="grid"))

print("#18")
print(tabulate(clientes.getpagos(),headers=["Codigo Empleado Rep Ventas","Codigo CLiente","Codigo Empleado","Nombre","Apellidos"],tablefmt="grid"))

print("#19")
print(tabulate(clientes.getpagos(),headers=["Codigo Empleado Rep Ventas","Codigo CLiente","Codigo Empleado","Nombre","Apellidos"],tablefmt="grid"))
import os 
import modules as modules
import modules.getEmpleados as Empleados
import modules.getPago as Pago
import modules.getOficinas as Oficinas
import modules.getClients as Clientes
import modules.getProducto as Producto
import modules.getPedido as Pedido

def menu1():
    while True:
        print(f"""
                    ----MENU PRINCIPAL----
                    
                    1.Empleados
                    2.Pago
                    3.Oficinas
                    4.Clientes
                    5.Producto
                    6.Pedido
                    
                    X.Salir
            """)

        while True:
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

menu1()