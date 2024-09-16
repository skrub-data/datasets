import openml
from openml.datasets import create_dataset

from dating_profile import *

openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_dating_profile_df()

params = {
    'name': 'dating_profile',
    'description': 'Anonymized data of dating profiles from OkCupid',
    'creator': 'OkCupid',
    'contributor': None,
    'language': 'English',
    'licence': 'NA',
    'collection_date': 'NA',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'age',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': DATING_PROFILE_CONFIG.urlinfos[0].url,
    'paper_url': DATING_PROFILE_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
