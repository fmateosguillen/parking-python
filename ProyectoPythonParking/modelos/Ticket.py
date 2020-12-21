class Ticket():
    def __init__(self, matr_vehiculo, fecha, id_plaza, clave):
        self._matr_vehiculo = matr_vehiculo
        self._fecha = fecha
        self._id_plaza = id_plaza
        self._clave = clave

    @property
    def matr_vehiculo(self):
        return self._matr_vehiculo

    @property
    def fecha(self):
        return self._fecha

    @property
    def id_plaza(self):
        return self._id_plaza

    @property
    def clave(self):
        return self._clave

    @matr_vehiculo.setter
    def matr_vehiculo(self, newMatr_Vehiculo):
        return self._matr_vehiculo

    @fecha.setter
    def fecha(self, newFecha):
        return self._fecha

    @id_plaza.setter
    def id_plaza(self, newId_Plaza):
        self._id_plaza = newId_Plaza

    @clave.setter
    def clave(self, newClave):
        self._clave = newClave
