import openml
from openml.datasets import create_dataset

from met_objects import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
df = get_met_objects_df()

params = {
    'name': 'met_objects',
    'description': 'The Metropolitan Museum of Art presents over 5,000 years of art from around the world for '
                   'everyone to experience and enjoy. The Museum lives in three iconic sites in New York City The Met '
                   'Fifth Avenue, The Met Breuer, and The Met Cloisters. Millions of people also take part in The Met '
                   'experience online.',
    'creator': 'The Museum of Modern Art',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2016-09-09',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Is_Public_Domain',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': MET_OBJECTS_CONFIG.urlinfos[0].url,
    'paper_url': MET_OBJECTS_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
