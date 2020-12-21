import pickle
from io import open
from datetime import datetime, timedelta
from modelos.Plaza import Plaza

fichero = open('ficheros/parking.pckl', 'rb')
parking = pickle.load(fichero)
fichero.close()

class Parking_Service():
    def cargar(self):
        fi1 = open('ficheros/lista_clientes.pckl', 'rb')
        clientes = pickle.load(fi1)
        fi1.close()
        parking.lista_clientes = clientes

        fi2 = open('ficheros/recaudacion.pckl', 'rb')
        recaudacion = pickle.load(fi2)
        fi2.close()
        parking.recaudacion = recaudacion

        fi3 = open('ficheros/recaudacion_abonos.pckl', 'rb')
        recaudacion_abonos = pickle.load(fi3)
        fi3.close()
        parking.recaudacion_abonos = recaudacion_abonos

    def get_parking(self):
        return parking

    def update_parking(self, newParking):
        f = open('ficheros/parking.pckl', 'wb')
        pickle.dump(newParking, f)
        f.close()

    def crear_plazas(self, num):
        num_turismos = round((num * 70)/100)
        num_motos = round((num * 15)/100)
        num_mov_red = round((num * 15)/100)
        parking.plazas_turismos = []
        parking.plazas_motos = []
        parking.plazas_mov_red = []

        for i in range(0, num_turismos):
            newPlaza = Plaza(int(i) + 1, "libre", None)
            parking.plazas_turismos.append(newPlaza)

        for i in range(0, num_motos):
            newPlaza = Plaza(int(i) + 1 + len(parking.plazas_turismos), "libre", None)
            parking.plazas_motos.append(newPlaza)

        for i in range(0, num_mov_red):
            newPlaza = Plaza(int(i) + 1 + len(parking.plazas_turismos) + (parking.plazas_motos), "libre", None)
            parking.plazas_mov_red.append(newPlaza)


    def get_plazas_libres(self):
        cont_turismos = len(parking.plazas_turismos)
        cont_motos = len(parking.plazas_motos)
        cont_mov_red = len(parking.plazas_mov_red)
        for i in parking.plazas_turismos:
            if i.estado != "libre":
                cont_turismos = cont_turismos - 1

        for i in parking.plazas_motos:
            if i.estado != "libre":
                cont_motos = cont_motos - 1

        for i in parking.plazas_mov_red:
            if i.estado != "libre":
                cont_mov_red = cont_mov_red - 1

    def get_plaza(self, vehiculo):
        for i in parking.plazas_turismos:
            if i.vehiculo == vehiculo:
                return i.id

        for i in parking.plazas_motos:
            if i.vehiculo == vehiculo:
                return i.id

        for i in parking.plazas_mov_red:
            if i.vehiculo == vehiculo:
                return i.id

    def comprobar_plazas(self):
        for i in parking.plazas_turismos:
            print("T --> ID: " + str(i.id) + ", ESTADO: " + i.estado)
        for i in parking.plazas_motos:
            print("M --> ID: " + str(i.id) + ", ESTADO: " + i.estado)
        for i in parking.plazas_mov_red:
            print("MR --> ID: " + str(i.id) + ", ESTADO: " + i.estado)

    def asignar_plaza(self, newVehiculo):
        plaza = Plaza(None, None, None)
        if newVehiculo.tipo == "1":
            for i in parking.plazas_turismos:
                if i.estado == "libre":
                    i.vehiculo = newVehiculo
                    i.estado = "ocupado"

        if newVehiculo.tipo == "2":
            for i in parking.plazas_motos:
                if i.estado == "libre":
                    i.vehiculo = newVehiculo
                    i.estado = "ocupado"

        if newVehiculo.tipo == "3":
            for i in parking.plazas_mov_red:
                if i.estado == "libre":
                    i.vehiculo = newVehiculo
                    i.estado = "ocupado"

    def asignar_plaza_abono(self, newVehiculo):
        plaza = Plaza(None, None, None)
        if newVehiculo.tipo == "1":
            for i in parking.plazas_turismos:
                if i.estado == "libre":
                    i.vehiculo = newVehiculo
                    return i

        if newVehiculo.tipo == "2":
            for i in parking.plazas_motos:
                if i.estado == "libre":
                    i.vehiculo = newVehiculo
                    return i

        if newVehiculo.tipo == "3":
            for i in parking.plazas_mov_red:
                if i.estado == "libre":
                    i.vehiculo = newVehiculo
                    return i

    def retirar_vehiculo(self, matricula, id, clave):
        for i in parking.plazas_turismos:
            if i.id == id:
                i.estado = "libre"
                i.vehiculo = None
                now = datetime.now()
                parking.recaudacion += 5 * 0.12

        for i in parking.plazas_motos:
            if i.id == id:
                i.estado = "libre"
                i.vehiculo = None
                now = datetime.now()
                parking.recaudacion += 5*0.08

        for i in parking.plazas_mov_red:
            if i.id == id:
                i.estado = "libre"
                i.vehiculo = None
                now = datetime.now()
                parking.recaudacion += 5*0.45

    def get_recaudacion(self):
        return parking.recaudacion

    def comprobar_abono(self, dni):
        encontrado = False
        for i in parking.lista_clientes:
            if i.dni == dni:
                encontrado = True
        return encontrado

    def get_cliente(self, dni):
        for i in parking.lista_clientes:
            if i.dni == dni:
                return i

    def get_plaza_cliente(self, cliente):
        return cliente.plaza

    def save_client(self, cliente):
        parking.lista_clientes.append(cliente)
        fichero = open('ficheros/lista_cllientes.pckl', 'wb')
        pickle.dump(parking.lista_clientes, fichero)
        fichero.close()

    def aparcar_abonado(self, plaza):
        for i in parking.plazas_turismos:
            if i.id == plaza.id:
                i.estado = "ocupado(A)"
        for i in parking.plazas_motos:
            if i.id == plaza.id:
                i.estado = "ocupado(A)"
        for i in parking.plazas_mov_red:
            if i.id == plaza.id:
                i.estado = "ocupado(A)"

    def comprobar_plaza(self, id):
        for i in parking.plazas_turismos:
            if i.id == id and i.estado == "ocupado(A)":
                return True

        for i in parking.plazas_motos:
            if i.id == id and i.estado == "ocupado(A)":
                return True

        for i in parking.plazas_mov_red:
            if i.id == id and i.estado == "ocupado(A)":
                return True

    def retirar_abonado(self, matricula, id, clave):
        for i in parking.plazas_turismos:
            if i.id == id:
                i.estado = "reservado"

        for i in parking.plazas_motos:
            if i.id == id:
                i.estado = "reservado"

        for i in parking.plazas_mov_red:
            if i.id == id:
                i.estado = "reservado"


    def calcular_fecha_fin_abono(self, tipo):
        fichero2 = open('ficheros/recaudacion_abonados.pckl', 'wb')
        if tipo == "1":
            fecha_fin = datetime.now() + timedelta(days=30)
            parking.recaudacion_abonos += 25
            pickle.dump(parking.recaudacion_abonos, fichero2)
            fichero2.close()
            return fecha_fin

        if tipo == "2":
            fecha_fin2 = datetime.now() + timedelta(days=90)
            parking.recaudacion_abonos += 70
            pickle.dump(parking.recaudacion_abonos, fichero2)
            fichero2.close()
            return fecha_fin2

        if tipo == "3":
            fecha_fin3 = datetime.now() + timedelta(days=180)
            parking.recaudacion_abonos += 130
            pickle.dump(parking.recaudacion_abonos, fichero2)
            fichero2.close()
            return fecha_fin3

        if tipo == "4":
            fecha_fin4 = datetime.now() + timedelta(days=365)
            parking.recaudacion_abonos += 200
            pickle.dump(parking.recaudacion_abonos, fichero2)
            fichero2.close()
            return fecha_fin4

    def mostrar_abonados(self):
        for i in parking.lista_clientes:
            print(i.nombre + " " + i.apellidos + " - TIPO ABONO:" + str(i.tipo_abono) + " F.INICIO: " + str(i.fecha_inicio_abono) + " // F.FIN: " + str(i.fecha_fin_abono))

    def mostrar_recaudacion_abonos(self):
        return parking.recaudacion_abonos

    def modificar_abonado(self, nombre, apellidos, dni, correo):
        for i in parking.lista_clientes:
            if i.dni == dni:
                i.nombre = nombre
                i.apellidos = apellidos
                i.correo = correo

    def borrar_abonado(self, dni):
        for i in parking.lista_clientes:
            if i.dni == dni:
                parking.lista_clientes.remove(i)
        fich = open('ficheros/lista_clientes.pckl', 'wb')
        pickle.dump(parking.lista_clientes, fich)
        fichero.close()
