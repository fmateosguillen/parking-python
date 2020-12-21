class Vehiculo():
    def __init__(self, modelo, matricula, tipo):
        self._modelo = modelo
        self._matricula = matricula
        self._tipo = tipo

    @property
    def modelo(self):
        return self._modelo

    @property
    def matricula(self):
        return self._matricula

    @property
    def tipo(self):
        return self._tipo

    @modelo.setter
    def modelo(self, newModelo):
        self._modelo = newModelo

    @matricula.setter
    def matricula(self, newMatricula):
        self._matricula = newMatricula

    @tipo.setter
    def tipo(self, newTipo):
        self._tipo = newTipo
