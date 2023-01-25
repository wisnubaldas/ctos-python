import pyodbc
# Bandung DB
# server = '192.168.100.100'
# database = 'dbWarehouse'
# username = 'sa'
# password = 'passwordsa'

server = '192.168.5.3'
database = 'dbWarehouse'
username = 'sa'
password = 'sa@123'

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Select Query

tsql = "SELECT * FROM EksporInvoice_Header;"
with cursor.execute(tsql):
    for row in cursor.fetchall():
        print(row[0])