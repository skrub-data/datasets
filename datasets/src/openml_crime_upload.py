import openml
from openml.datasets import create_dataset

from crime_data import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
df = get_crime_df()

params = {
    'name': 'la_crimes',
    'description': 'This dataset reflects incidents of crime in the City of Los Angeles dating back to 2010. This '
                   'data is transcribed from original crime reports that are typed on paper and therefore there may '
                   'be some inaccuracies within the data. Address fields are only provided to the nearest hundred '
                   'block in order to maintain privacy. This data is as accurate as the data in the database. Please '
                   'note questions or concerns in the comments.',
    'creator': 'LAPD',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2017-04-19',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Crime_Code_1',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': CRIME_DATA_CONFIG.urlinfos[0].url,
    'paper_url': CRIME_DATA_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
