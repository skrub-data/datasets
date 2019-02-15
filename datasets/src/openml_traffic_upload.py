import openml
from openml.datasets import create_dataset

from traffic_violations import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
df = get_traffic_violations_df()

params = {
    'name': 'Traffic_violations',
    'description': 'This dataset contains traffic violation information from all electronic traffic violations issued '
                   'in the County. Any information that can be used to uniquely identify the vehicle, the vehicle '
                   'owner or the officer issuing the violation will not be published.',
    'creator': 'data.montgomerycountymd.gov',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2015-02-04',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Violation_type',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': TRAFFIC_VIOLATIONS_CONFIG.urlinfos[0].url,
    'paper_url': TRAFFIC_VIOLATIONS_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
