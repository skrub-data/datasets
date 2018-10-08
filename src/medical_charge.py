import os
import pandas
from collections import namedtuple
from common.file_management import fetch, write_df

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
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
    main_file="medical_provider_charge_inpatient.csv",
    source="https://www.cms.gov/Research-Statistics-Data-and-Systems/"
           "Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data"
           "/Inpatient.html"
)


def get_medical_charge_df(save=True):
    data_dir = fetch(MEDICAL_CHARGE_CONFIG)
    file = os.listdir(data_dir[0])[0]
    csv_path = os.path.join(data_dir[0], file)
    df = pandas.read_csv(csv_path)
    write_df(save, df, data_dir[1], MEDICAL_CHARGE_CONFIG.main_file)
    return df
