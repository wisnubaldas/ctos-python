# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from os import getenv
import pymssql
# import _mssql
import pyodbc;
import urllib
from sqlalchemy import create_engine
engine = create_engine('mssql+pyodbc:///?odbc_connect=' +
    urllib.parse.quote_plus('DRIVER={ODBC Driver 17 for SQL Server};SERVER=192.168.100.100;PORT=1433;DATABASE=dblogin;UID=sa;PWD=itmau;')
)
for row in engine.execute('select 6 * 7 as [Result];'):
    print(row.Result)

# def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # try:
    #     conn = pyodbc.connect(
    #         server='192.168.100.100',
    #         user='sa',
    #         password='itmau',
    #         database='dbLogin')
    #
    #     # conn.execute_query('SELECT * FROM LoginUser')
    #
    # except pyodbc.MssqlDatabaseException as e:
    #     # if e.number == 2714 and e.severity == 16:
    #         # table already existed, so quieten the error
    #         print('error')
    #     # else:
    #     #     raise  # re-raise real error
    # finally:
    #     conn.close()


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':