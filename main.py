from bandung import Bandung
import helper
import json


class Main:
    def __init__(self):
        self.bandung = Bandung()
        pass

    def get_data_inv(self):
        ok = self.bandung.getInvHeaderEks(helper.gen_time())
        # list = []
        for row in ok:
            j = helper.inv_schema(row)
            helper.post_erp_next(j)

            # jr = json.dumps(j)
            # print(jr)
    def get_data_imp(self):
        importInv = self.bandung.getInvHeaderImp(helper.gen_time())
        for row in importInv:
            j = helper.inv_schema(row)
            helper.post_erp_next(j)

### jalanin di sceduler coy
x = Main()
# x.get_data_inv()
x.get_data_imp()

# while True:
#     Main()
#     time.sleep(5)
