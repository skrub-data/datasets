
import openml
from openml.datasets import create_dataset

from public_procurement import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_public_procurement_df()

params = {
    'name': 'public_procurement',
    'description': """Public procurement data
for the European Economic Area, Switzerland, and the
Macedonia. 2015""",
    'creator': 'European Union open data',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2016-04-18',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'award_value_euro',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': PUBLIC_PROCUREMENT_CONFIG.urlinfos[0].url,
    'paper_url': PUBLIC_PROCUREMENT_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
