class Parking():
    def __init__(self, plazas_turismos, plazas_motos, plazas_mov_red, lista_clientes, recaudacion, recaudacion_abonos):
        self._plazas_turismos = plazas_turismos
        self._plazas_motos = plazas_motos
        self._plazas_mov_red = plazas_mov_red
        self._lista_clientes = lista_clientes
        self._recaudacion = recaudacion
        self._recaudacion_abonos = recaudacion_abonos

    @property
    def plazas_turismos(self):
        return self._plazas_turismos

    @property
    def plazas_motos(self):
        return self._plazas_motos

    @property
    def plazas_mov_red(self):
        return self._plazas_mov_red

    @property
    def lista_clientes(self):
        return self._lista_clientes

    @property
    def recaudacion(self):
        return self._recaudacion

    @property
    def recaudacion_abonos(self):
        return self._recaudacion_abonos



    @plazas_turismos.setter
    def plazas_turismos(self, newPlazas_Turismos):
        self._plazas_turismos = newPlazas_Turismos

    @plazas_motos.setter
    def plazas_motos(self, newPlazas_Motos):
        self._plazas_motos = newPlazas_Motos

    @plazas_mov_red.setter
    def plazas_mov_red(self, newPlazas_Mov_Red):
        self._plazas_mov_red = newPlazas_Mov_Red

    @lista_clientes.setter
    def lista_clientes(self, newLista_Clientes):
        self._lista_clientes = newLista_Clientes

    @recaudacion.setter
    def recaudacion(self, newRecaudacion):
        self._recaudacion = newRecaudacion

    @recaudacion_abonos.setter
    def recaudacion_abonos(self, newRecaudacion_Abonos):
        self._recaudacion_abonos = newRecaudacion_Abonos
