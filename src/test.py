from colleges import get_colleges_df
from crime_data import get_crime_df
from employee_salaries import get_employee_salaries_df
from journal_influence import get_journal_influence_df
from medical_charge import get_medical_charge_df
from met_objects import get_met_objects_df
from midwest_survey import get_midwest_survey_df
from open_payments import get_open_payment_df
from road_safety import get_road_safety_df
from traffic_violations import get_traffic_violations_df
from beer_reviews import get_beer_reviews_df
import asyncio

func_map = {
    'crime': get_crime_df,
    'colleges': get_colleges_df,
    'employee': get_employee_salaries_df,
    'journal': get_journal_influence_df,
    'medical': get_medical_charge_df,
    'met': get_met_objects_df,
    'midwest': get_midwest_survey_df,
    'road': get_road_safety_df,
    'traffic': get_traffic_violations_df,
    'open payment': get_open_payment_df,
    'beer review': get_beer_reviews_df
}


async def run(name, func):
    print('Getting', name.upper(), 'data')
    df = func()
    assert (df is not None)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [
        asyncio.ensure_future(run(f, func_map[f])) for f in func_map
    ]

    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
