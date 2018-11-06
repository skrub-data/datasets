import openml
from openml.datasets import create_dataset

from midwest_survey import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'

df = get_midwest_survey_df()

params = {
    'name': 'Midwest survey',
    'description': 'Survey to know if people self-identify as Midwesterners.',
    'creator': 'FiveThiryEight.com',
    'contributor': None,
    'language': 'English',
    'licence': 'Creative Commons Attribution 4.0 International License',
    'collection_date': '2014-04-30',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Location (Census Region)',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': MIDWEST_SURVEY_CONFIG.urlinfos[0].url,
    'paper_url': MIDWEST_SURVEY_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
