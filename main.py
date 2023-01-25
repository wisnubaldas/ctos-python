from bandung import Bandung
import time
import json
import collections

class Main:
    def __init__(self):
        self.get_data_inv()
    def get_data_inv(self):

        data = Bandung()
        ok = data.select("SELECT * FROM EksporInvoice_Header where "
                         "DateOfTransaction = '2019-07-25' and "
                         "TimeOfTransaction BETWEEN '03:20' AND '03:24';")
        rowarray_list = []
        for row in ok:
            t = collections.OrderedDict()
            t['invoice_number'] = row[0]
            rowarray_list.append(t)
        j = json.dumps(rowarray_list)
        print(j)

Main()
# while True:
#     Main()
#     time.sleep(5)