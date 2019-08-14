import openml
from openml.datasets import create_dataset

from wine_reviews import get_wine_reviews_df

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_wine_reviews_df()

params = {
    'name': 'wine_reviews',
    'description': 'Wine data gathered by https://www.kaggle.com/zynicide'
                   'The data was scraped from WineEnthusiast during the week of June 15th, 2017. The code for the scraper can be found at https://github.com/zackthoutt/wine-deep-learning',
    'creator': 'https://www.winemag.com',
    'contributor': 'https://www.kaggle.com/zynicide',
    'language': 'English',
    'licence': 'CC BY-NC-SA 4.0',
    'collection_date': '2017-06-15',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'points',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': 'https://www.kaggle.com/zynicide/wine-reviews/home#winemag-data_first150k.csv',
    'paper_url': None,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
