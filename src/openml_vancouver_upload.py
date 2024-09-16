import openml
from openml.datasets import create_dataset

from vancouver_employee import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_vancouver_employee_df()

desc = """Employee remuneration and expenses (earning over 75,000CAD per year). This data set includes remuneration and expenses from employees earning over 75,000CAD per year.

    Attributes:
    NAME: Name of employee listed by last name, followed by initials of first name and middle name (if applicable)
    DEPARTMENT: Name of an organization unit at the City of Vancouver where specified Title belongs
    TITLE: Name of position
    REMUNERATION: Includes salary, overtime, gratuity and vacation payouts. Excludes severance payment.
    EXPENSES: Includes charges such as training, tuition, conferences and travel and professional dues"""
# desc = 'Employee of Vancouver remenuration'
params = {
    'name': 'vancouver_employee',
    'description': desc,
    'creator': 'City of Vancouver',
    'contributor': None,
    'language': 'English',
    'licence': 'Open Government Licence Vancouver',
    'collection_date': '2017-08-13',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'remuneration',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': 'https://data.vancouver.ca/datacatalogue/employeeRemunerationExpensesOver75k.htm',  #VANCOUVER_EMPLOYEE_CONFIG.urlinfos[0].url,
    'paper_url': VANCOUVER_EMPLOYEE_CONFIG.source,
    'update_comment': None
}

# from openml_beer_upload import params
# params['name'] = 'vancouver_employee'
dset = create_dataset(**params)
open_ml_id = dset.publish()
