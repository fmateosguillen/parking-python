import pickle
from io import open
from datetime import datetime, timedelta
import random
from modelos.Cliente import Cliente
from modelos.Ticket import Ticket
from modelos.Vehiculo import Vehiculo
from servicios.parking_service import Parking_Service
from servicios.ticket_service import Ticket_Service

p = Parking_Service()
opcion, opcion2, opcion3 = int, int, int
password = 0000

p.cargar()
print("¡Bienvenido a ParKKing!")
while opcion != 0:
    try:
        print("Indique de que forma quiere acceder:\n")
        print("1. Acceder como cliente")
        print("2. Acceder como administrador")
        print("0. Salir\n")
        opcion = int(input())
        if opcion != 1 and opcion != 2 and opcion != 0:
            raise ValueError
        else:
            if opcion == 1:
                while opcion2 != 0:
                    try:
                        print("Indique la acción que desea realizar")
                        print("1. Depositar vehículo")
                        print("2. Retirar vehículo")
                        print("3. Depositar vehiculo abonado")
                        print("4. Retirar vehiculo abonado")
                        print("0. Salir")
                        opcion2 = int(input())
                        if opcion2 != 1 and opcion2 != 2 and opcion2 != 3 and opcion2 != 4 and opcion2 != 0:
                            raise ValueError
                        else:
                            if opcion2 == 1 :
                                p.get_plazas_libres()
                                modelo = str(input('Indique el modelo de su vehículo'))
                                matricula = int(input('Introduzca la matrícula de su vehículo'))
                                tipo_vehiculo = input("Seleccione el tipo de vehículo que quiere almacenar:\n1. Turismo\n2. Motocicleta\n3. Vehículo para personas con movilidad reducida")
                                newVehiculo = Vehiculo(modelo, matricula, tipo_vehiculo)
                                p.asignar_plaza(newVehiculo)
                                m = datetime.now()
                                clave = random.randint(0000, 9999)
                                ticket = Ticket(matricula, m, p.get_plaza(newVehiculo), clave)
                                ts = Ticket_Service(ticket)
                                ts.guardar()
                                ts.imprimir_ticket()
                            elif opcion2 == 2:
                                matricula2 = input('Introduzca la matrícula de su vehículo')
                                id = int(input('Introduzca el modelo de la plaza: '))
                                clave = int(input('Introduzca el PIN: '))
                                p.retirar_vehiculo(matricula2, id, clave)
                                print("Ya puede recoger su vehículo")
                            elif opcion2 == 3:
                                autenticacion = input('Introduzca su dni para comprobar su abono: ')
                                if p.comprobar_abono(autenticacion):
                                    p.asignar_plaza_abono(p.get_plaza_cliente(p.get_cliente(autenticacion)))
                                    print("Su vehículo ha sido depositado correctamente")
                                else:
                                    print("Los datos introducidos no coinciden con ningún abono")
                            elif opcion2 == 4:
                                autenticacion2 = input('Introduzca la matrícula de su vehículo:')
                                id2 = int(input('Introduzca el id de la plaza en la que está estacionado su vehículo:'))
                                clave2 = int(input('Introduzca la clave para retirar el vehículo: '))
                                if p.comprobar_plaza(id2):
                                    p.retirar_abonado(autenticacion2, id2, clave)
                                    print("Ya puede recoger su vehículo (Esta plaza está reservada para usted, vuelva pronto)")
                                else:
                                    print("Los datos introducidos no corresponden con ningún abono o su vehículo no está en el parking")
                            elif opcion2 == 0:
                                break
                    except ValueError:
                        print("La opción introducida no es correcta (inserte el número que está a la izquierda de la opción que quiera escoger)")
            elif opcion == "2":
                admin_password = int(input("Introduzca su contraseña de administrador: "))
                if admin_password == password:
                    while opcion3 != 0:
                        try:
                            print("Indique la acción que desea realizar:\n")
                            print("1. Mostrar el estado del parking")
                            print("2. Mostrar recaudación")
                            print("3. Crear un nuevo parking")
                            print("4. Consultar abonados")
                            print("5. Agregar abonado")
                            print("6. Borrar abonado")
                            print("7. Editar abonado")
                            print("0. Salir\n")
                            opcion3 = int(input())
                            if opcion3 != 1 and opcion3 != 2 and opcion3 != 3 and opcion3 != 4 and opcion3 != 5 and opcion3 != 6 and opcion3 != 7 and opcion3 != 0:
                                raise ValueError
                            else:
                                if opcion3 == 1:
                                    p.comprobar_plazas()
                                elif opcion3 == 2:
                                    print("RECAUDACIÓN: "+ str(p.get_recaudacion()) + "€")
                                elif opcion3 == 3:
                                    num_plazas = input("Introduzca el número de plazas totales que tendrá el parking (NOTA: El 70% serán asignadas a turismos, el 15% a motocicletas y el 15% restante a vehículos de movilidad reducida): ")
                                    p.crear_plazas(num_plazas)
                                    print("El parking se creó exitosamente\n")
                                elif opcion3 == 4:
                                    p.mostrar_abonados()
                                    print("RECAUDACIÓN POR ABONOS: "+ str(p.mostrar_recaudacion_abonos()) + " euros")
                                elif opcion3 == 5:
                                    nombre = input("Introduzca el nombre del cliente: ")
                                    apellidos = input("Introduzca los apellidos del cliente: ")
                                    dni = input('Introduzca el dni del cliente: ')
                                    num_tarj = int(input("Introduzca el número de la tarjeta del cliente: "))
                                    tipo_abono = input("Introduzca el tipo de abono deseado por el cliente (1: Mensual, 2: Trimestral, 3: Semestral, 4: Anual): ")
                                    correo = input("Introduzca la dirección de correo electrónico del cliente: ")
                                    fecha_inicio_abono = datetime.now()
                                    clave = random.randint(0000, 9999)
                                    matr_cliente = int(input("Introduzca la matrícula del cliente: "))
                                    tipo_veh = input("Introduzca el tipo de vehículo del cliente (1: Turismo, 2: Motocicleta, 3: Vehículo para personas con movilidad reducida): ")
                                    veh = Vehiculo(matr_cliente, tipo_veh)
                                    new_cliente = Cliente(dni, nombre, apellidos, num_tarj, tipo_abono, correo, veh, p.asignar_plaza_abono(veh), clave, fecha_inicio_abono, p.calcular_fecha_fin_abono(tipo_abono))
                                    p.save_client(new_cliente)
                                    print("El abono se asignó al cliente exitosamente")
                                elif opcion3 == 6:
                                    dni2 = input('Introduce el dni del cliente que deseas eliminar: ')
                                    p.borrar_abonado(dni2)
                                    print("El cliente ha sido eliminado exitosamente")
                                elif opcion3 == 7:
                                    dni3 = input("Introduce el dni del abonado que deseas editar: ")
                                    new_name = input("Introduce el nombre editado: ")
                                    new_apellidos = input("Introduce los apellidos editados: ")
                                    new_correo = input("Introduce el correo editado: ")
                                    p.modificar_abonado(dni3, new_name, new_apellidos, new_correo)
                                    print("Los datos del abonado fueron modificados exitosamente")
                                elif opcion3 == 0:
                                    break
                        except ValueError:
                            print("La opción introducida no es correcta (inserte el número que está a la izquierda de la opción que quiera escoger)")
                else:
                    print("Acceso Denegado")
                    break
            elif opcion == "0":
                break
    except ValueError:
        print("La opción introducida no es correcta (inserte el número que está a la izquierda de la opción que quiera escoger)")
p.update_parking(p.get_parking())
print("¡Hasta Pronto!")




