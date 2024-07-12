import openml
from openml.datasets import create_dataset

from employee_salaries import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
df = get_employee_salaries_df()

params = {
    'name': 'employee_salaries',
    'description': 'Annual salary information including gross pay and overtime pay for all active, permanent '
                   'employees of Montgomery County, MD paid in calendar year 2016. This information will be published '
                   'annually each year.',
    'creator': 'Office of Human Resources, Montgomery County OpenData',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2017-02-21',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Current_Annual_Salary',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': EMPLOYEE_SALARIES_CONFIG.urlinfos[0].url,
    'paper_url': EMPLOYEE_SALARIES_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
