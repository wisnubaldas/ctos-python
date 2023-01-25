import pyodbc


class Bandung:
        def __init__(self):
            server = '192.168.5.3'
            database = 'dbWarehouse'
            username = 'sa'
            password = 'sa@123'
            cnxn = pyodbc.connect(
                'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            self.cursor = cnxn.cursor()

        def select(self, sql):
            self.cursor.execute(sql)
            return self.cursor.fetchall()
