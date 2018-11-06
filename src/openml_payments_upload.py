import openml
from openml.datasets import create_dataset

from open_payments import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'

df = get_open_payment_df()

params = {
    'name': 'Open Payments',
    'description': 'Payments given by healthcare manufacturing companies to medical doctors or hospitals',
    'creator': 'Centers for Medicare & Medicaid Services',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2018-01-01',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Status',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': OPEN_PAYMENTS_CONFIG.urlinfos[0].url,
    'paper_url': OPEN_PAYMENTS_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
