import pickle
from modelos.Cliente import Cliente
from modelos.Parking import Parking
from modelos.Plaza import Plaza
from modelos.Vehiculo import Vehiculo
from datetime import datetime, timedelta
from io import open

plaza_turismo1 = Plaza(1, "libre", None)
plaza_turismo2 = Plaza(2, "libre", None)
plaza_turismo3 = Plaza(3, "libre", None)
plaza_turismo4 = Plaza(4, "libre", None)
plaza_turismo5 = Plaza(5, "libre", None)
plaza_turismo6 = Plaza(6, "libre", None)
plaza_turismo7 = Plaza(7, "libre", None)
plaza_turismo8 = Plaza(8, "libre", None)
plaza_turismo9 = Plaza(9, "libre", None)
plaza_turismo10 = Plaza(10, "libre", None)
plaza_turismo11 = Plaza(11, "libre", None)
plaza_turismo12 = Plaza(12, "libre", None)
plaza_turismo13 = Plaza(13, "libre", None)
plaza_turismo14 = Plaza(14, "libre", None)
plaza_turismo15 = Plaza(15, "libre", None)
plaza_turismo16 = Plaza(16, "libre", None)
plaza_turismo17 = Plaza(17, "libre", None)
plaza_turismo18 = Plaza(18, "libre", None)
plaza_turismo19 = Plaza(19, "libre", None)
plaza_turismo20 = Plaza(20, "libre", None)
plaza_turismo21 = Plaza(21, "libre", None)
plaza_turismo22 = Plaza(22, "libre", None)
plaza_turismo23 = Plaza(23, "libre", None)
plaza_turismo24 = Plaza(24, "libre", None)
plaza_turismo25 = Plaza(25, "libre", None)
plaza_turismo26 = Plaza(26, "libre", None)
plaza_turismo27 = Plaza(27, "libre", None)
plaza_turismo28 = Plaza(28, "libre", None)
plaza_turismo29 = Plaza(29, "libre", None)
plaza_turismo30 = Plaza(30, "libre", None)
plaza_turismo31 = Plaza(31, "libre", None)
plaza_turismo32 = Plaza(32, "libre", None)
plaza_turismo33 = Plaza(33, "libre", None)
plaza_turismo34 = Plaza(34, "libre", None)
plaza_turismo35 = Plaza(35, "libre", None)
plaza_turismo36 = Plaza(36, "libre", None)
plaza_turismo37 = Plaza(37, "libre", None)
plaza_turismo38 = Plaza(38, "libre", None)
plaza_turismo39 = Plaza(39, "libre", None)
plaza_turismo40 = Plaza(40, "libre", None)
plaza_turismo41 = Plaza(41, "libre", None)
plaza_turismo42 = Plaza(42, "libre", None)
plaza_turismo43 = Plaza(43, "libre", None)
plaza_turismo44 = Plaza(44, "libre", None)
plaza_turismo45 = Plaza(45, "libre", None)
plaza_turismo46 = Plaza(46, "libre", None)
plaza_turismo47 = Plaza(47, "libre", None)
plaza_turismo48 = Plaza(48, "libre", None)
plaza_turismo49 = Plaza(49, "libre", None)
plaza_turismo50 = Plaza(50, "libre", None)
plaza_turismo51 = Plaza(51, "libre", None)
plaza_turismo52 = Plaza(52, "libre", None)
plaza_turismo53 = Plaza(53, "libre", None)
plaza_turismo54 = Plaza(54, "libre", None)
plaza_turismo55 = Plaza(55, "libre", None)
plaza_turismo56 = Plaza(56, "libre", None)
plaza_turismo57 = Plaza(57, "libre", None)
plaza_turismo58 = Plaza(58, "libre", None)
plaza_turismo59 = Plaza(59, "libre", None)
plaza_turismo60 = Plaza(60, "libre", None)
plaza_turismo61 = Plaza(61, "libre", None)
plaza_turismo62 = Plaza(62, "libre", None)
plaza_turismo63 = Plaza(63, "libre", None)
plaza_turismo64 = Plaza(64, "libre", None)
plaza_turismo65 = Plaza(65, "libre", None)
plaza_turismo66 = Plaza(66, "libre", None)
plaza_turismo67 = Plaza(67, "libre", None)
plaza_turismo68 = Plaza(68, "libre", None)
plaza_turismo69 = Plaza(69, "libre", None)
plaza_turismo70 = Plaza(70, "libre", None)

plazas_turismos = [plaza_turismo1,plaza_turismo2, plaza_turismo3, plaza_turismo4, plaza_turismo5, plaza_turismo6
    , plaza_turismo7, plaza_turismo8, plaza_turismo9, plaza_turismo10, plaza_turismo11, plaza_turismo12, plaza_turismo12
    , plaza_turismo13, plaza_turismo14, plaza_turismo15, plaza_turismo16, plaza_turismo17, plaza_turismo18, plaza_turismo19
    , plaza_turismo20, plaza_turismo21, plaza_turismo22, plaza_turismo23, plaza_turismo24, plaza_turismo25, plaza_turismo26
    , plaza_turismo27, plaza_turismo28, plaza_turismo29, plaza_turismo30, plaza_turismo31, plaza_turismo32, plaza_turismo33
    , plaza_turismo34, plaza_turismo35, plaza_turismo36, plaza_turismo37, plaza_turismo38, plaza_turismo39, plaza_turismo40
    , plaza_turismo41, plaza_turismo42, plaza_turismo43, plaza_turismo44, plaza_turismo45, plaza_turismo46, plaza_turismo47
    , plaza_turismo48, plaza_turismo49, plaza_turismo50, plaza_turismo51, plaza_turismo52, plaza_turismo53, plaza_turismo54
    , plaza_turismo55, plaza_turismo56, plaza_turismo57, plaza_turismo58, plaza_turismo59, plaza_turismo60, plaza_turismo61
    , plaza_turismo62, plaza_turismo63, plaza_turismo64, plaza_turismo65, plaza_turismo66, plaza_turismo67, plaza_turismo68
    , plaza_turismo69, plaza_turismo70]

plaza_moto1 = Plaza(71, "libre", None)
plaza_moto2 = Plaza(72, "libre", None)
plaza_moto3 = Plaza(73, "libre", None)
plaza_moto4 = Plaza(74, "libre", None)
plaza_moto5 = Plaza(75, "libre", None)
plaza_moto6 = Plaza(76, "libre", None)
plaza_moto7 = Plaza(77, "libre", None)
plaza_moto8 = Plaza(78, "libre", None)
plaza_moto9 = Plaza(79, "libre", None)
plaza_moto10 = Plaza(80, "libre", None)
plaza_moto11 = Plaza(81, "libre", None)
plaza_moto12 = Plaza(82, "libre", None)
plaza_moto13 = Plaza(83, "libre", None)
plaza_moto14 = Plaza(84, "libre", None)
plaza_moto15 = Plaza(85, "libre", None)

plazas_motos = [plaza_moto1, plaza_moto2, plaza_moto3, plaza_moto4, plaza_moto5, plaza_moto6, plaza_moto7, plaza_moto8
    , plaza_moto9, plaza_moto10, plaza_moto11, plaza_moto12, plaza_moto13, plaza_moto14, plaza_moto15]

plaza_mov_red1 = Plaza(86, "libre", None)
plaza_mov_red2 = Plaza(87, "libre", None)
plaza_mov_red3 = Plaza(88, "libre", None)
plaza_mov_red4 = Plaza(89, "libre", None)
plaza_mov_red5 = Plaza(90, "libre", None)
plaza_mov_red6 = Plaza(91, "libre", None)
plaza_mov_red7 = Plaza(92, "libre", None)
plaza_mov_red8 = Plaza(93, "libre", None)
plaza_mov_red9 = Plaza(94, "libre", None)
plaza_mov_red10 = Plaza(95, "libre", None)
plaza_mov_red11 = Plaza(96, "libre", None)
plaza_mov_red12 = Plaza(97, "libre", None)
plaza_mov_red13 = Plaza(98, "libre", None)
plaza_mov_red14 = Plaza(99, "libre", None)
plaza_mov_red15 = Plaza(100, "libre", None)

plazas_mov_red = [plaza_mov_red1, plaza_mov_red2, plaza_mov_red3, plaza_mov_red4, plaza_mov_red5, plaza_mov_red6
    , plaza_mov_red7, plaza_mov_red8, plaza_mov_red9, plaza_mov_red10, plaza_mov_red11, plaza_mov_red12, plaza_mov_red13
    , plaza_mov_red14, plaza_mov_red15]

vehiculo = Vehiculo("Toyota Auris", "9324JPG", 1)
fecha_inicio = datetime.now()
fecha_fin = fecha_inicio + timedelta(days=30)

c1 = Cliente("Francisco Javier", "Mateos Guillén", "29534419G", 1602, 1, "fmateosguillen@gmail.com", vehiculo, plaza_turismo24, 123456, fecha_inicio, fecha_fin)
lista_clientes = [c1]

fichero1 = open('../ficheros/lista_clientes.pckl', 'wb')
pickle.dump(lista_clientes, fichero1)
fichero1.close()
fichero1 = open('../ficheros/lista_clientes.pckl', 'rb')
clientes = pickle.load(fichero1)
fichero1.close()

parking = Parking(plazas_turismos, plazas_motos, plazas_mov_red, clientes, None, None)
parking.recaudacion = 1000
parking.recaudacion = 300

fichero2 = open('../ficheros/recaudacion.pckl', 'wb')
pickle.dump(parking.recaudacion, fichero2)
fichero2.close()

fichero3 = open('../ficheros/recaudacion_abonos', 'wb')
pickle.dump(parking.recaudacion_abonos, fichero3)
fichero3.close()

listado_tickets = []
fichero4 = open('../ficheros/tickets.pckl', 'wb')
pickle.dump(listado_tickets, fichero4)
fichero4.close()

fichero = open('../ficheros/parking.pckl', 'wb')
pickle.dump(parking, fichero)
fichero.close()
