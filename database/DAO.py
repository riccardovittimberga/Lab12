from database.DB_connect import DBConnect
from model.metodo import Metodo
from model.product import Product


class DAO():

    @staticmethod
    def getAllMethods():

        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * from go_methods gds  """

        cursor.execute(query)

        for row in cursor:
            result.append(Metodo(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProductsN(metodo,anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct Product_number as pn
                    from go_daily_sales gds 
                     where gds.Order_method_code=%s and YEAR(gds.date)=%s"""

        cursor.execute(query,(metodo,anno))

        for row in cursor:
            result.append((row['pn']))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllProducts():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select * 
                        from go_products gds """

        cursor.execute(query)

        for row in cursor:
            result.append(Product(**row))

        cursor.close()
        conn.close()
        return result
