class Plaza():
    def __init__(self, id, estado, vehiculo):
        self._id = id
        self._estado = estado
        self._vehiculo = vehiculo

    @property
    def id(self):
        return self._id

    @property
    def estado(self):
        return self._estado

    @property
    def vehiculo(self):
        return self._vehiculo



    @id.setter
    def id(self, newId):
        self._id = newId

    @estado.setter
    def estado(self, newEstado):
        self._estado = newEstado

    @vehiculo.setter
    def vehiculo(self, newVehiculo):
        self._vehiculo = newVehiculo
