from colleges import get_colleges_df
from crime_data import get_crime_df
from open_payments import get_open_payment_df
from employee_salaries import get_employee_salaries_df
from journal_influence import get_journal_influence_df
from medical_charge import get_medical_charge_df
from met_objects import get_met_objects_df
from midwest_survey import get_midwest_survey_df
from road_safety import get_road_safety_df
from traffic_violations import get_traffic_violations_df

# import os
# import shutil
# TODO: At least do a dummy test and check if files are downloaded and outputs generated

print("Getting traffic violations")
get_traffic_violations_df()

print("Getting road safety")
get_road_safety_df()

print("Getting midwest survey")
get_midwest_survey_df()

print("Getting met objects")
get_met_objects_df()

print("Getting medical charge")
get_medical_charge_df()

print("Getting journal influence")
get_journal_influence_df()

print("Getting employee salaries")
get_employee_salaries_df()

print("Getting open payment")
get_open_payment_df()

print("Getting crime")
get_crime_df()

print("Getting colleges")
get_colleges_df()

