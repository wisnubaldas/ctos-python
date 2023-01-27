import collections
import arrow
import requests
import saveToLocal
import json

erpNext = 'https://erp.ctos.inidev.xyz/api/method/ctoserp.ctoserp.invoiceCTOS'


def set_eksp_file(jml):
    exp_file = open('file/exp_file', 'w')
    exp_file.writelines(jml)
    exp_file.close()


def get_eksp_file():
    exp_file = open('file/exp_file', 'r')
    nmr = exp_file.readline()
    exp_file.close()
    return nmr


def post_erp_next(data):
    r = requests.post(erpNext, json=data)
    if r.status_code == 200:
        rs = r.json()
        saveToLocal.create_respon((
            rs['status'],
            r.text
        ))
    elif r.status_code == 500:
        saveToLocal.create_error(
            data[1],
            'Error kirim data'
        )
    print(data)
    saveToLocal.create_data_inv(data['NO_INVOICE'], json.dumps(data))


def gen_time():
    end_time = arrow.utcnow().to('Asia/Jakarta')
    start_time = end_time.shift(minutes=-5)
    return (
        start_time.format('YYYY-MM-HH'),
        start_time.format('HH:mm'),
        end_time.format('HH:mm')
    )


def inv_schema(row):
    t = collections.OrderedDict()
    t['COMPANY'] = row[0]
    t['CUSTUMER_CODE'] = row[1]
    t['NO_INVOICE'] = row[2]
    t['TANGGAL'] = row[3] + ' ' + row[4]
    t['PAYMENT_CODE'] = row[5]
    t['SMU'] = row[6]
    t['HAWB'] = row[7]
    t['KDAIRLINE'] = row[8]
    t['FLIGHT_NUMBER'] = row[9]
    t['DOM_INT'] = row[10]
    t['INC_OUT'] = row[11]
    t['ASAL'] = row[12]
    t['TUJUAN'] = row[13]
    t['JENIS_KARGO'] = row[14]
    t['TARIF_KARGO'] = int(row[15])
    t['KOLI'] = float(row[16])
    t['BERAT'] = float(row[17])
    t['VOLUME'] = float(row[18])
    t['JML_HARI'] = int(row[19])
    t['CARGO_CHG'] = float(row[20])
    t['KADE'] = float(row[21])
    t['TOTAL_PENDAPATAN_TANPA_PPN'] = float(row[22])
    t['TOTAL_PENDAPATAN_DENGAN_PPN'] = float(row[23])
    t['PJT_HANDLING_FEE'] = float(row[24])
    t['RUSH_HANDLING_FEE'] = float(row[25])
    t['RUSH_SERVICE_FEE'] = float(row[26])
    t['TRANSHIPMENT_FEE'] = float(row[27])
    t['ADMINISTRATION_FEE'] = float(row[28])
    t['DOCUMENTS_FEE'] = float(row[29])
    t['PECAH_PU_FEE'] = float(row[30])
    t['COOL_COLD_STORAGE_FEE'] = float(row[31])
    t['STRONG_ROOM_FEE'] = float(row[32])
    t['AC_ROOM_FEE'] = float(row[33])
    t['DG_ROOM_FEE'] = float(row[34])
    t['AVI_ROOM_FEE'] = float(row[35])
    t['DANGEROUS_GOOD_CHECK_FEE'] = float(row[36])
    t['DISCOUNT_FEE'] = float(row[37])
    t['RKSP_FEE'] = float(row[38])
    t['HAWB_FEE'] = float(row[39])
    t['HAWB_MAWB_FEE'] = float(row[40])
    t['CSC_FEE'] = float(row[41])
    t['ENVIROTAINER_ELEC_FEE'] = float(row[42])
    t['ADDITIONAL_COSTS'] = float(row[43])
    t['NAWB_FEE'] = float(row[44])
    t['BARCODE_FEE'] = float(row[45])
    t['CARGO_DEVELOPMENT_FEE'] = float(row[46])
    t['DUTIABLE_SHIPMENT_FEE'] = float(row[47])
    t['FHL_FEE'] = float(row[48])
    t['FWB_FEE'] = float(row[49])
    t['CARGO_INSPECTION_REPORT_FEE'] = float(row[50])
    t['MATERAI_FEE'] = float(row[51])
    t['PPN_FEE'] = float(row[52])
    t['VOID'] = bool(row[53])
    return t
