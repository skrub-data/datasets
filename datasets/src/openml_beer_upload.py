import openml
from openml.datasets import create_dataset

from beer_reviews import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
df = get_beer_reviews_df()

params = {
    'name': 'beer_reviews',
    'description': 'This dataset consists of beer reviews from Beeradvocate. The data span a period of more than 10 '
                   'years, including all ~1.5 million reviews up to November 2011. Each review includes ratings in '
                   'terms of five "aspects": appearance, aroma, palate, taste, and overall impression. Reviews '
                   'include product and user information, followed by each of these five ratings, and a plaintext '
                   'review. We also have reviews from ratebeer.',
    'creator': 'socialmediadata',
    'contributor': None,
    'language': 'English',
    'licence': 'Public',
    'collection_date': '2016-09-30',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Beer_Style',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': BEER_REVIEWS_CONFIG.urlinfos[0].url,
    'paper_url': BEER_REVIEWS_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
