import pickle
from io import open
from datetime import datetime, timedelta
import random
from modelos.Ticket import Ticket
from modelos.Vehiculo import Vehiculo

class Ticket_Service():
    def __init__(self, ticket):
        self._ticket = ticket

    def guardar(self):
        fichero = open('ficheros/lista_clientes.pckl', 'rb')
        tickets = pickle.load(fichero)
        fichero.close()
        tickets.append(self._ticket)
        fichero = open('ficheros/tickets.pckl', 'wb')
        pickle.dump(tickets, fichero)
        fichero.close()

    def imprimir_ticket(self):
        print("##################################")
        print("               TICKET             ")
        print("##################################")
        print("    FECHA: " + str(self._ticket.fecha)+"    ")
        print("")
        print("    MATRICULA: " + str(self._ticket.matr_vehiculo) + "    ")
        print("")
        print("    CLAVE: " + str(self._ticket.clave) + "    ")
        print("##################################")
