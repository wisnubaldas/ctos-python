from bandung import Bandung
import helper
import json


class Main:
    def __init__(self):
        pass

    def get_data_inv(self):
        data = Bandung()
        ok = data.get_inv_header(helper.gen_time())
        list = []
        for row in ok:
            list.append(helper.inv_schema(row))
            j = json.dumps(list)
            print(j)




x = Main()
x.get_data_inv()

# while True:
#     Main()
#     time.sleep(5)
