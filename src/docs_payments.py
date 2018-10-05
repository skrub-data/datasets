import os
import pandas
from collections import namedtuple
from common.file_management import fetch

DatasetInfo = namedtuple('DatasetInfo',
                         ['name', 'urlinfos', 'main_file', 'source'])
# a DatasetInfo Object is basically a tuple of UrlInfos object
# an UrlInfo object is composed of an url and the filenames contained
# in the request content
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

OPEN_PAYMENTS_CONFIG = DatasetInfo(
    name='open_payments',
    urlinfos=
    (
        UrlInfo(
            url='http://download.cms.gov/openpayments/PGYR13_P011718.ZIP',
            filenames=None, uncompress=True
        ),
    ),
    main_file='OP_DTL_GNRL_PGYR2013_P01172018.csv',  # same
    source='https://openpaymentsdata.cms.gov'
)

data_dir = fetch(OPEN_PAYMENTS_CONFIG)
file = os.listdir(data_dir)[0]
csv_path = os.path.join(data_dir, file)
df = pandas.read_csv(csv_path)


'''
DEBUG
THIS DOES NOT UNZIP... NEED TO CHECK IT OUT
'''