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

MEDICAL_CHARGE_CONFIG = DatasetInfo(
    name='medical_charge',
    urlinfos=(
        UrlInfo(
            url="https://www.cms.gov/Research-Statistics-Data-and-Systems/"
                "Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/"
                "Downloads/Inpatient_Data_2011_CSV.zip",
            filenames=(
                "MedicalProviderChargeInpatient.csv",
            ),
            uncompress=True

        ),
    ),
    main_file="MedicalProviderChargeInpatient.csv",
    source="https://www.cms.gov/Research-Statistics-Data-and-Systems/"
           "Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data"
           "/Inpatient.html"
)

data_dir = fetch(MEDICAL_CHARGE_CONFIG)
file = os.listdir(data_dir)[0]
csv_path = os.path.join(data_dir, file)
df = pandas.read_csv(csv_path)
