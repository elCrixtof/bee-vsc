def create_order_detail(self, id_order, id_product, od_amount, od_total):
          try:
               sql = 'INSERT INTO order_details (`id_order`,`id_product`, `od_amount`, `od_total`) VALUES (%s,%s,%s,%s)'
               vals = (id_order, id_product, od_amount, od_total)
               self.cursor.execute(sql, vals)
               self.cnx.commit()
               return True
          except connector.Error as err:
               self.cnx.rollback()
               return(err)


# create table if not exists riesgo_nutricio(
# 	nua varchar(06) not null,
#     periodo varchar(30) not null,
#     padecimiento_actual varchar(50),
#     cirugias varchar(50),
#     tratamiento varchar(50),
#     n_comidas int not null,
#     desayuno boolean not null,
#     comida boolean not null,
#     cena boolean not null,
#     colaciones boolean not null,
#     hora_apetito varchar(20) not null,
#     lugar_comida varchar(30) not null,
#     cocinero varchar(30) not null,
#     servicios_basicos boolean not null,
#     cantidad_agua float(6,2) not null,
#     consumo_tablaco boolean not null,
#     cantidad_tabaco float(6,2) not null,
#     consumo_alcohol boolean not null,
#     cantidad_alcohol float(6,2) not null,
#     consumo_azucar boolean not null,
#     cantidad_azucar float(6,2) not null,
#     criterio_1 varchar(200) not null,
# 	criterio_2 varchar(200) not null,
# 	criterio_3 varchar(200) not null,
# 	criterio_4 varchar(200) not null,
# 	criterio_5 varchar(200) not null,
#     diagnostico varchar(200) not null,
#     institucion varchar(60) not null,
#     primary key (nua, periodo),
#     constraint fk_riesgo_alumno foreign key(nua)
# 		references alumno(nua)
#         on delete cascade
#         on update cascade
# )engine = innodb;