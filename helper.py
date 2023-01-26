import collections
import arrow


def set_eksp_file(jml):
    exp_file = open('file/exp_file', 'w')
    exp_file.writelines(jml)
    exp_file.close()


def get_eksp_file():
    exp_file = open('file/exp_file', 'r')
    nmr = exp_file.readline()
    exp_file.close()
    return nmr


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
    t['CUSTUMER_CODE'] = row[0]
    t['NO_INVOICE'] = row[0]
    t['TANGGAL'] = row[0]
    t['PAYMENT_CODE'] = row[0]
    t['SMU'] = row[0]
    t['HAWB'] = row[0]
    t['KDAIRLINE'] = row[0]
    t['FLIGHT_NUMBER'] = row[0]
    t['DOM_INT'] = row[0]
    t['INC_OUT'] = row[0]
    t['ASAL'] = row[0]
    t['TUJUAN'] = row[0]
    t['JENIS_KARGO'] = row[0]
    t['TARIF_KARGO'] = row[0]
    t['KOLI'] = row[0]
    t['BERAT'] = row[0]
    t['VOLUME'] = row[0]
    t['JML_HARI'] = row[0]
    t['CARGO_CHG'] = row[0]
    t['KADE'] = row[0]
    t['TOTAL_PENDAPATAN_TANPA_PPN'] = row[0]
    t['TOTAL_PENDAPATAN_DENGAN_PPN'] = row[0]
    t['PJT_HANDLING_FEE'] = row[0]
    t['RUSH_HANDLING_FEE'] = row[0]
    t['RUSH_SERVICE_FEE'] = row[0]
    t['TRANSHIPMENT_FEE'] = row[0]
    t['ADMINISTRATION_FEE'] = row[0]
    t['DOCUMENTS_FEE'] = row[0]
    t['PECAH_PU_FEE'] = row[0]
    t['COOL_COLD_STORAGE_FEE'] = row[0]
    t['STRONG_ROOM_FEE'] = row[0]
    t['AC_ROOM_FEE'] = row[0]
    t['DG_ROOM_FEE'] = row[0]
    t['AVI_ROOM_FEE'] = row[0]
    t['DANGEROUS_GOOD_CHECK_FEE'] = row[0]
    t['DISCOUNT_FEE'] = row[0]
    t['RKSP_FEE'] = row[0]
    t['HAWB_FEE'] = row[0]
    t['HAWB_MAWB_FEE'] = row[0]
    t['CSC_FEE'] = row[0]
    t['ENVIROTAINER_ELEC_FEE'] = row[0]
    t['ADDITIONAL_COSTS'] = row[0]
    t['NAWB_FEE'] = row[0]
    t['BARCODE_FEE'] = row[0]
    t['CARGO_DEVELOPMENT_FEE'] = row[0]
    t['DUTIABLE_SHIPMENT_FEE'] = row[0]
    t['FHL_FEE'] = row[0]
    t['FWB_FEE'] = row[0]
    t['CARGO_INSPECTION_REPORT_FEE'] = row[0]
    t['MATERAI_FEE'] = row[0]
    t['PPN_FEE'] = row[0]
    t['VOID'] = row[0]
    return t
