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
            url='http://download.cms.gov/openpayments/PGYR13_P062918.ZIP',
            # url='https://openpaymentsdata.cms.gov/api/views/xi5e-hzfv/rows.csv?accessType=DOWNLOAD',
            filenames=None, uncompress=True
        ),
    ),
    main_file='OP_DTL_GNRL_PGYR2013_P01172018.csv',  # same
    source='https://openpaymentsdata.cms.gov'
)


def _get_file_paths(directory):
    f = [os.path.join(directory, file) for file in os.listdir(directory) if
         '.txt' not in file and 'REMOVED' not in file]
    return f


def get_docs_payment_df(save=True):
    data_dir = fetch(OPEN_PAYMENTS_CONFIG)
    files = _get_file_paths(data_dir)
    dfs = [pandas.read_csv(file) for file in files]
    df = pandas.concat(objs=dfs, axis=0, join='outer', keys=['A', 'B', 'C'], sort=True)
    if save:
        df.to_csv('docs_payments_df.csv', chunksize=10000, compression='gzip')
    return df


get_docs_payment_df()
