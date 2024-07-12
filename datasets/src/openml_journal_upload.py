import openml
from openml.datasets import create_dataset

from journal_influence import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'

df = get_journal_influence_df()
params = {
    'name': 'article_influence',
    'description': 'Estimated article influence scores in 2015',
    'creator': 'Bree Norlander',
    'contributor': None,
    'language': 'English',
    'licence': 'CC BY 4.0',
    'collection_date': '2018-04-13',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'journal_name',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': JOURNAL_INFLUENCE_CONFIG.urlinfos[0].url,
    'paper_url': JOURNAL_INFLUENCE_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
