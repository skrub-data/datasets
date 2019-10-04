import openml
from openml.datasets import create_dataset

from house_sales import get_house_sales_df

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_house_sales_df()

params = {
    'name': 'house_sales',
    'description': """This dataset contains house sale prices for King County, which includes Seattle. It includes homes sold between May 2014 and May 2015.

It contains 19 house features plus the price and the id columns, along with 21613 observations.
It's a great dataset for evaluating simple regression models.
""",
    'creator': 'https://www.kaggle.com/harlfoxem/',
    'contributor': 'https://www.kaggle.com/harlfoxem/',
    'language': 'English',
    'licence': 'CC0 Public Domain',
    'collection_date': '2016-08-25',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'price',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': 'https://www.kaggle.com/harlfoxem/housesalesprediction',
    'paper_url': None,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
