import openml
from openml.datasets import create_dataset

from drug_discovery import *

openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_drug_discovery_df()

params = {
    'name': 'drug_directory',
    'description': 'Product listing data submitted'
    'to the U.S. FDA for all unfinished, unapproved drugs.',
    'creator': 'FDA',
    'contributor': None,
    'language': 'English',
    'licence': 'NA',
    'collection_date': 'NA',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'product_type_name',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': DRUG_DISCOVERY_CONFIG.urlinfos[0].url,
    'paper_url': DRUG_DISCOVERY_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
