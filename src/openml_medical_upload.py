import openml
from openml.datasets import create_dataset

from medical_charge import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
df = get_medical_charge_df()

params = {
    'name': 'medical_charges',
    'description': 'The Inpatient Utilization and Payment Public Use File (Inpatient PUF) provides information on '
                   'inpatient discharges for Medicare fee-for-service beneficiaries. The Inpatient PUF includes '
                   'information on utilization, payment (total payment and Medicare payment), and hospital-specific '
                   'charges for the more than 3,000 U.S. hospitals that receive Medicare Inpatient Prospective '
                   'Payment System (IPPS) payments. The PUF is organized by hospital and Medicare Severity Diagnosis '
                   'Related Group (MS-DRG) and covers Fiscal Year (FY) 2011 through FY 2016.',
    'creator': 'Centers for Medicare & Medicaid Services',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2018-08-14',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Average_total_payments',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': MEDICAL_CHARGE_CONFIG.urlinfos[0].url,
    'paper_url': MEDICAL_CHARGE_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
with open('medical.xml', 'w+') as file:
    file.write(dset._to_xml())
open_ml_id = dset.publish()
print(open_ml_id)