from bandung import Bandung
class Conn:
    def __init__(self):
        pass
    def db_bandung(self):
        # Bandung DB
        server = '192.168.100.100'
        database = 'dbWarehouse'
        username = 'sa'
        password = 'passwordsa'

        cnxn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = cnxn.cursor()
    def db_jkt(self):
        server = '192.168.5.3'
        database = 'dbWarehouse'
        username = 'sa'
        password = 'sa@123'

        cnxn = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cnxn.cursor()

