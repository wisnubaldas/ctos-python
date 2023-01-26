import pyodbc

class Bandung:
        def __init__(self):
            server = '192.168.5.3'
            database = 'dbWarehouse'
            username = 'sa'
            password = 'sa@123'
            try:
                cnxn = pyodbc.connect(
                    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
                self.cursor = cnxn.cursor()
            except pyodbc.Error as e:
                print(e)
        def get_inv_header(self,dt):
            sql = "SELECT * FROM EksporInvoice_Header " \
                  "where DateOfTransaction = '"+dt[0]+"' AND " \
                  "TimeOfTransaction BETWEEN '"+dt[1]+"' AND '"+dt[2]+"';"
            self.cursor.execute(sql)
            return self.cursor.fetchall()

        def count_eksport_inv(self):
            sql = "SELECT COUNT(*) FROM EksporInvoice_Header"
            self.cursor.execute(sql)
            return self.cursor.fetchval()
