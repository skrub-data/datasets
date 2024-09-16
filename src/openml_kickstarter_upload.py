import openml
from openml.datasets import create_dataset

from kickstarter_projects import get_kickstarter_projects_df

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_kickstarter_projects_df()

params = {
    'name': 'kickstarter_projects',
    'description': """
    Data are collected from Kickstarter Platform

You'll find most useful data for project analysis. Columns are self explanatory except:

usd_pledged: conversion in US dollars of the pledged column (conversion done by kickstarter).

usd pledge real: conversion in US dollars of the pledged column (conversion from Fixer.io API).

usd goal real: conversion in US dollars of the goal column (conversion from Fixer.io API).


""",
    'creator': 'https://www.kickstarter.com/',
    'contributor': 'https://www.kaggle.com/kemical',
    'language': 'English',
    'licence': 'CC BY-NC-SA 4.0',
    'collection_date': '2018-01-15',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'state',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': 'https://www.kaggle.com/kemical/kickstarter-projects',
    'paper_url': None,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
