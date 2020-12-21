class Cliente():
    def __init__(self, nombre, apellidos, dni, num_tarj, tipo_abono, correo, vehiculo, plaza, clave, fecha_inicio_abono, fecha_fin_abono):
        self._nombre = nombre
        self._apellidos = apellidos
        self._dni = dni
        self._num_tarj = num_tarj
        self._tipo_abono = tipo_abono
        self._correo = correo
        self._vehiculo = vehiculo
        self._plaza = plaza
        self._clave = clave
        self._fecha_inicio_abono = fecha_inicio_abono
        self._fecha_fin_abono = fecha_fin_abono

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellidos(self):
        return self._apellidos

    @property
    def dni(self):
        return self._dni

    @property
    def num_tarj(self):
        return self._num_tarj

    @property
    def tipo_abono(self):
        return self._tipo_abono

    @property
    def correo(self):
        return self._correo

    @property
    def vehiculo(self):
        return self._vehiculo

    @property
    def plaza(self):
        return self._plaza

    @property
    def clave(self):
        return self._clave

    @property
    def fecha_inicio_abono(self):
        return self._fecha_inicio_abono

    @property
    def fecha_fin_abono(self):
        return self._fecha_fin_abono



    @nombre.setter
    def nombre(self, newNombre):
        self._nombre = newNombre

    @apellidos.setter
    def apellidos(self, newApellidos):
        self._apellidos = newApellidos

    @dni.setter
    def dni(self, newDni):
        self._dni = newDni

    @num_tarj.setter
    def num_tarj(self, newNum_Tarj):
        self._num_tarj = newNum_Tarj

    @tipo_abono.setter
    def tipo_abono(self, newTipo_Abono):
        self._tipo_abono = newTipo_Abono

    @correo.setter
    def correo(self, newCorreo):
        self._correo = newCorreo

    @vehiculo.setter
    def vehiculo(self, newVehiculo):
        self._vehiculo = newVehiculo

    @plaza.setter
    def plaza(self, newPlaza):
        self._plaza = newPlaza

    @clave.setter
    def clave(self, newClave):
        self._clave = newClave

    @fecha_inicio_abono.setter
    def fecha_inicio_abono(self, newFecha_Inicio_Abono):
        self._fecha_inicio_abono = newFecha_Inicio_Abono

    @fecha_fin_abono.setter
    def fecha_fin_abono(self, newFecha_Fin_Abono):
        self._fecha_fin_abono = newFecha_Fin_Abono
