import openml
from openml.datasets import create_dataset

from federal_election import *

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_federal_election_df()

params = {
    'name': 'federal_election',
    'description': """General Description
2015-current: greater than $200.00. The Commission categorizes contributions from individuals using the calendar year-to-date amount for political action committee (PAC) and party committee receipts and the election-cycle-to-date amount for candidate receipts to determine whether the contribution meets the categorization threshold of greater than $200.00.

1989-2014: $200 and above. The Commission categorized contributions from individuals using the reporting period amount to determine whether a contribution met the categorization threshold of $200.00 or more.

1975-1988: $500 and above. The Commission categorized contributions from individuals using the reporting period amount to determine whether a contribution met the categorization threshold of $500.00 or more.

header description can be found here : https://classic.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml
""",
    'creator': 'Federal Election Commission',
    'contributor': None,
    'language': 'English',
    'licence': 'NA',
    'collection_date': '2015-08-13',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'transaction_amt',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': FEDERAL_ELECTION_CONFIG.urlinfos[0].url,
    'paper_url': FEDERAL_ELECTION_CONFIG.source,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
