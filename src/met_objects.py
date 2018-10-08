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

MET_OBJECTS_CONFIG = DatasetInfo(
    name='met_objects',
    urlinfos=(
        UrlInfo(
            url='https://github.com/metmuseum/openaccess/raw/master/MetObjects.csv',
            filenames=(
                "MetObjects.csv",
            ), uncompress=False
        ),
    ),
    main_file="MetObjects.csv",
    source="https://github.com/metmuseum/openaccess/raw/master/"
)

data_dir = fetch(MET_OBJECTS_CONFIG)
file = os.listdir(data_dir)[0]
csv_path = os.path.join(data_dir, file)
df = pandas.read_csv(csv_path)
