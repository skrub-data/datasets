import os
from collections import namedtuple

import numpy as np
import pandas as pd
import xlrd

from .common.file_management import fetch, write_df, float_to_int

DatasetInfo = namedtuple('DatasetInfo', ['name', 'urlinfos', 'main_file', 'source'])
UrlInfo = namedtuple('UrlInfo', ['url', 'filenames', 'uncompress'])

ROAD_SAFETY_CONFIG = DatasetInfo(
    name='road_safety',
    urlinfos=(
        UrlInfo(
            url="http://data.dft.gov.uk/road-accidents-safety-data/"
                "RoadSafetyData_2015.zip",
            filenames=(
                "Casualties_2015.csv",
                "Vehicles_2015.csv",
                "Accidents_2015.csv"
            ),
            uncompress=True),
        UrlInfo(
            url="http://data.dft.gov.uk/road-accidents-safety-data/"
                "MakeModel2015.zip",
            filenames=("2015_Make_Model.csv",),
            uncompress=True
        ),
        UrlInfo(
            url="http://data.dft.gov.uk/road-accidents-safety-data/"
                "Road-Accident-Safety-Data-Guide.xls",
            filenames=("Road-Accident-Safety-Data-Guide.xls",),
            uncompress=False
        )
    ),
    main_file="road_safety_2015.csv",
    source="https://data.gov.uk/dataset/road-accidents-safety-data"
)

MAPPING_COL_TO_DESCR = {
    'Vehicle_Type': 'Vehicle Type',
    'Towing_and_Articulation': 'Towing and Articulation',
    'Vehicle_Manoeuvre': 'Vehicle Manoeuvre',
    'Junction_Location': 'Junction Location',
    'Vehicle_Location-Restricted_Lane': 'Vehicle Location',
    'Skidding_and_Overturning': 'Skidding and Overturning',
    'Hit_Object_in_Carriageway': 'Hit Object in Carriageway',
    'Vehicle_Leaving_Carriageway': 'Veh Leaving Carriageway',
    'Hit_Object_off_Carriageway': 'Hit Object Off Carriageway',
    '1st_Point_of_Impact': '1st Point of Impact',
    'Was_Vehicle_Left_Hand_Drive?': 'Was Vehicle Left Hand Drive',
    'Was_Vehicle_Left_Hand_Drive': 'Was Vehicle Left Hand Drive',
    'Journey_Purpose_of_Driver': 'Journey Purpose',
    'Sex_of_Driver': 'Sex of Driver',
    'Age_Band_of_Driver': 'Age Band',
    'Propulsion_Code': 'Vehicle Propulsion Code',
    'Driver_IMD_Decile': 'IMD Decile',
    'Driver_Home_Area_Type': 'Home Area Type',
    'Casualty_Class': 'Casualty Class',
    'Sex_of_Casualty': 'Sex of Casualty',
    'Age_Band_of_Casualty': 'Age Band',
    'Casualty_Severity': 'Casualty Severity',
    'Pedestrian_Location': 'Ped Location',
    'Pedestrian_Movement': 'Ped Movement',
    'Car_Passenger': 'Car Passenger',
    'Bus_or_Coach_Passenger': 'Bus Passenger',
    'Pedestrian_Road_Maintenance_Worker': 'Ped Road Maintenance Worker',
    'Casualty_Type': 'Casualty Type',
    'Casualty_Home_Area_Type': 'Home Area Type',
    'Casualty_IMD_Decile': 'IMD Decile',
    'Police_Force': 'Police Force',
    'Accident_Severity': 'Accident Severity',
    'Day_of_Week': 'Day of Week',
    'Local_Authority_(District)': 'Local Authority (District)',
    'Local_Authority_(Highway)': 'Local Authority (Highway)',
    '1st_Road_Class': '1st Road Class',
    '2nd_Road_Class': '2nd Road Class',
    'Road_Type': 'Road Type',
    'Junction_Detail': 'Junction Detail',
    'Junction_Control': 'Junction Control',
    'Pedestrian_Crossing-Physical_Facilities': 'Ped Cross - Physical',
    'Pedestrian_Crossing-Human_Control': 'Ped Cross - Human',
    'Light_Conditions': 'Light Conditions',
    'Weather_Conditions': 'Weather',
    'Road_Surface_Conditions': 'Road Surface',
    'Special_Conditions_at_Site': 'Special Conditions at Site',
    'Carriageway_Hazards': 'Carriageway Hazards',
    'Urban_or_Rural_Area': 'Urban Rural',
    'Did_Police_Officer_Attend_Scene_of_Accident': 'Police Officer Attend'
}


def _get_file_paths(directory):
    f = dict(description=os.path.join(directory, "Road-Accident-Safety-Data-Guide.xls"),
             data=[os.path.join(directory, elt) for elt in os.listdir(directory) if
                   elt != "Road-Accident-Safety-Data-Guide.xls"])
    return f


def _denormalize(df, descr):
    description = xlrd.open_workbook(descr)

    for name in df.keys():
        if name in MAPPING_COL_TO_DESCR:
            sheet = description.sheet_by_name(MAPPING_COL_TO_DESCR[name])
            x = sheet.first_visible_rowx + 1
            mapping = {sheet.cell_value(j, 0): sheet.cell_value(j, 1) for j in range(x, sheet.nrows)}
            result_array = []

            for r in df[name]:
                try:
                    result_array.append(mapping[r])
                except KeyError:
                    result_array.append("Nan")

            df[name] = result_array

    return df


def _process_df(files):
    res_df = pd.DataFrame()
    for file in files['data']:
        df = pd.read_csv(file)

        if 'Accidents_2015.csv' not in file:
            df['Vehicle_Reference'] = (df['Vehicle_Reference'].map(str))

        df = df.set_index('Accident_Index')
        if '2015_Make_Model.csv' in file:
            df = df.dropna(axis=0, how='any', subset=['make'])

        df = _denormalize(df, files['description'])

        if res_df.empty:
            res_df = df
        else:
            res_df = res_df.join(df, how='left', lsuffix='_df_res', rsuffix='_df')

    res_df = res_df.dropna(axis=0, how='any', subset=['make'])
    return res_df


def get_road_safety_df(save=True):
    data_dir = fetch(ROAD_SAFETY_CONFIG)
    files = _get_file_paths(data_dir[0])
    df = _process_df(files)
    f_to_i = ['1st_Road_Number', '2nd_Road_Number', 'Location_Easting_OSGR', 'Location_Northing_OSGR',
              'Number_of_Vehicles', 'Number_of_Casualties', 'Speed_limit', 'accyr', 'Engine_Capacity_(CC)_df',
              'Age_of_Vehicle_df']
    str_to_i = ['Vehicle_Reference', 'Vehicle_Reference_df', 'Vehicle_Reference_df_res']
    to_del = ['data missing or out of range', 'none', -1, 'unknown or other', 'not known', 'unclassified', 'unknown',
              'nan']

    for c in df:
        tab = []
        for elt in df[c]:
            if (isinstance(elt, str) and elt.lower() in to_del) or elt in to_del:
                tab.append(np.nan)
            else:
                tab.append(elt)
        df[c] = pd.Series(tab, dtype=np.object, index=df.index)

    for c in f_to_i:
        df[c] = float_to_int(df[c], df.index)

    for c in str_to_i:
        tab = []
        for elt in df[c]:
            if isinstance(elt, str):
                tab.append(int(elt))
            else:
                tab.append(elt)
        df[c] = pd.Series(tab, dtype=np.object, index=df.index)

    for c in df:
        if len(df[c].unique()) == 1 and str(df[c].unique()[0]) == 'nan':
            df.drop([c], 1, inplace=True)

    write_df(save, df, data_dir[1], ROAD_SAFETY_CONFIG.main_file)
    return df
