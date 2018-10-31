import openml
from openml.datasets import create_dataset

from employee_salaries import *


def send_dataset(name, description, creator, contributor, language, licence, collection_date, attributes, data,
                 ignore_attribute, default_target_attribute, row_id_attribute, citation, version_label,
                 original_data_url, paper_url, update_comment):
    params = {
        'name': name,
        'description': description,
        'creator': creator,
        'contributor': contributor,
        'language': language,
        'licence': licence,
        'collection_date': collection_date,
        'attributes': attributes,
        'data': data,
        'ignore_attribute': ignore_attribute,
        'default_target_attribute': default_target_attribute,
        'row_id_attribute': row_id_attribute,
        'citation': citation,
        'version_label': version_label,
        'original_data_url': original_data_url,
        'paper_url': paper_url,
        'update_comment': update_comment
    }

    return create_dataset(**params)


df = get_employee_salaries_df()
params = {
    'name': 'employee_salaries',
    'description': 'description',
    'creator': 'Office of Human Resources, Montgomery County OpenData',
    'contributor': None,
    'language': 'English',
    'licence': 'Public Domain (CC0)',
    'collection_date': '2017-02-21',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Current_Annual_Salary',
    'row_id_attribute': list(df.keys()[0]),
    'citation': None,
    'version_label': '0.1',
    'original_data_url': EMPLOYEE_SALARIES_CONFIG.urlinfos[0].url,
    'paper_url': EMPLOYEE_SALARIES_CONFIG.source,
    'update_comment': None
}

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'

dset = send_dataset(**params)
id = dset.publish()
print(id)
