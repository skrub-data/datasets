import openml
from openml.datasets import create_dataset

from building_permits import get_building_permits_df

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_building_permits_df()

# print('use head  ! ' * 100)
# df = df.head(n=15)

desc = """This dataset includes information about currently-valid building permits issued by the City of Chicago from 2006 to the present. Building permits are issued subject to payment of applicable fees. If building or zoning permit fees show as unpaid, the permit is not valid. (A permit is valid if only 'other fees' are shown as unpaid.) This dataset does not include permits which have been issued and voided or revoked. This dataset also does not include permits for mechanical amusement riding devices and carnivals issued by the Department of Buildings.

Property Index Numbers (PINs) and geographic information (ward, community area and census tract) are provided for most permit types issued in 2008 or later.
"""

params = {
    'name': 'building_permits',
    'description': desc,
    'creator': 'Chicago city',
    'contributor': 'https://www.kaggle.com/chicago',
    'language': 'English',
    'licence': 'CC0 Public Domain',
    'collection_date': '2019-08-13',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'estimated_cost',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': 'https://www.kaggle.com/chicago/chicago-building-permits',
    'paper_url': None,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
