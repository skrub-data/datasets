# link dataset name to their id in openml.org

# this list of datasets are from "Encoding high-cardinality string categorical variables"
# https://arxiv.org/pdf/1907.01860.pdf

dataset_id = {
"building_permits" :  None,
"beer_reviews" : 42088,
"colleges" : 42159,
"crime_data" : 42160,
"drug_directory" : None,
"employe_salaries" : 42125,
"federal_election" : 42080,
"journal_influence" : 42123,
"kickstarter_projects" : 42076,
"medical_charge" : 42131,
"met_objects" : None,
"midwest_survey" : None,
"open_payment" : None,
"public_procurement" : None,
"road_safety" : None,
"traffic_violations" : None,
"vancouver_employee" : 42089,
"wine_reviews" : 42074,

"Adult" : 1590,
"cacao_flavor" : 42133,
"california_housing" : 537,
"dating_profile" : None,
"house_prices" : None,
"house_sales" : 42092,
"intrusion_detection" : None,
}

from sklearn.datasets import fetch_openml

def test_fetch_openml():
    # fetch all dataset currently available
    for name, id in dataset_id.items():
        if id is not None:
            print('fetch ', name)
            # requiered sklearn >= 0.22 !!
            data = fetch_openml(data_id = id, as_frame=True)
            print('- data shape:', data['data'].shape)



