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

CRIME_DATA_CONFIG = DatasetInfo(
    name='crime_data',
    urlinfos=(
        UrlInfo(
            url="https://data.lacity.org/api/views/y8tr-7khq/rows.csv?accessType=DOWNLOAD",
            filenames=(
                "Crime_Data_from_2010_to_Present.csv",
            ), uncompress=True
        ),
    ),
    main_file="Crime_Data_from_2010_to_Present.csv",
    source="https://catalog.data.gov/dataset/crime-data-from-2010-to-present"
)

data_dir = fetch(CRIME_DATA_CONFIG)
file = os.listdir(data_dir)[0]
csv_path = os.path.join(data_dir, file)
df = pandas.read_csv(csv_path)
