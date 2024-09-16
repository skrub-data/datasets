import openml
from openml.datasets import create_dataset

from house_price import *

openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_house_price_df()

desc = ''.join(open('data/house-prices/data_description.txt').readlines())
params = {
    'name': 'house_prices',
    'description': desc,
    'creator': 'OkCupid',
    'contributor': None,
    'language': 'English',
    'licence': 'NA',
    'collection_date': 'NA',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'SalePrice',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': HOUSE_PRICE_CONFIG.urlinfos[0].url,
    'paper_url': HOUSE_PRICE_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
