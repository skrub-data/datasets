import openml
from openml.datasets import create_dataset

from road_safety import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'

df = get_road_safety_df()

params = {
    'name': 'Road safety',
    'description': 'Data reported to the police about the circumstances of per- sonal injury road accidents in Great '
                   'Britain from 1979, and the maker and model information of vehicles involved in the respective '
                   'accident',
    'creator': 'Department for Transport UK',
    'contributor': None,
    'language': 'English',
    'licence': 'Open Government License',
    'collection_date': '2018-10-12',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Sex of Driver',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': ROAD_SAFETY_CONFIG.urlinfos[0].url,
    'paper_url': ROAD_SAFETY_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
