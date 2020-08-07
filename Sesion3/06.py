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


