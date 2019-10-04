import openml
from openml.datasets import create_dataset

from colleges import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas

df = get_colleges_df()

params = {
    'name': 'colleges',
    'description': 'Regroups information for about 7800 different US colleges. Including geographical information, '
                   'stats about the population attending and post graduation career earnings.',
    'creator': 'NA',
    'contributor': None,
    'language': 'English',
    'licence': 'NA',
    'collection_date': 'NA',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'percent_pell_grant',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': COLLEGES_CONFIG.urlinfos[0].url,
    'paper_url': COLLEGES_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
