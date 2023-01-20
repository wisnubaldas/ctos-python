import pyodbc
server = '192.168.100.100'
database = 'dbWarehouse'
username = 'sa'
password = 'passwordsa'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# print ('Inserting a new row into table')
# #Insert Query
# tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
# with cursor.execute(tsql,'Jake','United States'):
#     print ('Successfully Inserted!')
#
#
# #Update Query
# print ('Updating Location for Nikita')
# tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
# with cursor.execute(tsql,'Sweden','Nikita'):
#     print ('Successfully Updated!')
#
#
# #Delete Query
# print ('Deleting user Jared')
# tsql = "DELETE FROM Employees WHERE Name = ?"
# with cursor.execute(tsql,'Jared'):
#     print ('Successfully Deleted!')


#Select Query
print ('Reading data from table')
tsql = "SELECT * FROM FareDirectory;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()