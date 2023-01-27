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
        def getInvHeaderImp(self,dt):
            sql = "SELECT company = 'MAU BDO', a.CustomerCode, a.InvoiceNumber,a.DateOfTransaction," \
                  "a.TimeOfTransaction, a.PaymentCode, b.MasterAWB,b.HostMAWB,a.AirlinesCode,d.FlightNumber," \
                  "domIn = 'I',inOut='I',d.OriginCode,dest = 'BDO',d.KindOfGood,tarigKargo = 0,a.TotalPieces," \
                  "a.TotalNetto,a.TotalCAW,b.OverStay,a.TotalWarehouseFee,b.AssistancyFee,a.SubTotalFee," \
                  "a.GrandTotalFee,pjt = 0,rushHandling = 0,rushService = 0,transhipment = 0," \
                  "a.AdministrationFee,a.DocumentFee,pecah_pu = 0,b.CoolRoomFee,b.StrongRoomFee,b.AirConditioningFee," \
                  "b.DangerousRoomFee,avi_room = 0,dgCheck = 0,discount = 0,rksp = 0,hawbFee = 0,mawbFee = 0,csc = 0," \
                  "eecf=0,addCost=0,nawbFee = 0,barcode = 0,cargoDev = 0,dutiFee = 0,fhlFee = 0, fwbFee = 0,cirfFee = 0,b.OtherFee,a.TaxFee,a.Void " \
                  "FROM ImportInvoice_Header AS a " \
                  "INNER JOIN ImportInvoice_Detail AS b ON a.InvoiceNumber = b.InvoiceNumber " \
                  "INNER JOIN ImportDeliveryOrder_Header AS c ON b.DeliveryOrderNumber = c.DeliveryOrderNumber " \
                  "INNER JOIN ImportDeliveryOrder_Detail AS d ON c.DeliveryOrderNumber = d.DeliveryOrderNumber " \
                  "WHERE a.DateOfTransaction = '2019-07-27' AND a.TimeOfTransaction BETWEEN '03:00' AND '22:00';"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        def getInvHeaderEks(self,dt):
            dt = list(dt)
            dt[0] = '2019-07-25'
            dt[1] = '03:20'
            dt[2] = '22:00'
            dt = tuple(dt)

            sql = "SELECT top 2 company = 'MAU BDO', a.CustomerCode, a.InvoiceNumber," \
                  "a.DateOfTransaction,a.TimeOfTransaction,a.PaymentCode, b.MasterAWB,d.HostAWB,a.AirlinesCode," \
                  "c.FlightNumber,domIn = 'I',inOut='O',c.Origin,c.Destination,d.KindOfNature,tarigKargo = 0," \
                  "a.TotalPieces," \
                  "a.TotalNetto,a.TotalCAW," \
                  "OverStay = 1,a.TotalWarehouseFee,b.AssistancyFee,a.SubTotalFee,a.GrandTotalFee," \
                  "pjt = 0,rushHandling = 0,rushService = 0,transhipment = 0,a.AdministrationFee," \
                  "a.DocumentFee,pecah_pu = 0,b.CoolRoomFee,b.StrongRoomFee,b.AirConditioningFee," \
                  "b.DangerousRoomFee,avi_room = 0,dgCheck = 0,discount = 0,rksp = 0,hawbFee = 0," \
                  "mawbFee = 0,csc = 0,eecf=0,addCost=0,nawbFee = 0,barcode = 0,cargoDev = 0,dutiFee = 0," \
                  "fhlFee = 0, fwbFee = 0,cirfFee = 0,materai = 0,a.TaxFee,a.Void " \
                  "FROM [dbo].[EksporInvoice_Header] AS a " \
                  "INNER JOIN EksporInvoice_Detail AS b ON a.InvoiceNumber = b.InvoiceNumber " \
                  "INNER JOIN EksporWeighingProof_Header as c ON b.ProofNumber = c.ProofNumber " \
                  "INNER JOIN EksporWeighingProof_Detail AS d ON c.ProofNumber = d.ProofNumber WHERE " \
                  "a.DateOfTransaction = '2019-07-27' AND a.TimeOfTransaction BETWEEN '03:00' AND '22:00';"
            self.cursor.execute(sql)
            return self.cursor.fetchall()

        def count_eksport_inv(self):
            sql = "SELECT COUNT(*) FROM EksporInvoice_Header"
            self.cursor.execute(sql)
            return self.cursor.fetchval()
