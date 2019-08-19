import openml
from openml.datasets import create_dataset

from cacao_flavor import get_cacao_flavor_df

openml.config.apikey = '58012f5a6cbba5dcd3ddefbf852c1e99'
openml.config.apikey = 'ca1d24f37f00a1517a1638d5acc24321'  # Thomas
df = get_cacao_flavor_df()

full_desc = """Chocolate Bar Ratings.
    Expert ratings of over 1,700 chocolate bars. Each chocolate is evaluated from a combination of both objective qualities and subjective interpretation. A rating here only represents an experience with one bar from one batch. Batch numbers, vintages and review dates are included in the database when known.

    The database is narrowly focused on plain dark chocolate with an aim of appreciating the flavors of the cacao when made into chocolate. The ratings do not reflect health benefits, social missions, or organic status.
    
    Flavor is the most important component of the Flavors of Cacao ratings. Diversity, balance, intensity and purity of flavors are all considered. It is possible for a straight forward single note chocolate to rate as high as a complex flavor profile that changes throughout. Genetics, terroir, post harvest techniques, processing and storage can all be discussed when considering the flavor component.
    
    Texture has a great impact on the overall experience and it is also possible for texture related issues to impact flavor. It is a good way to evaluate the makers vision, attention to detail and level of proficiency.
    
    Aftermelt is the experience after the chocolate has melted. Higher quality chocolate will linger and be long lasting and enjoyable. Since the aftermelt is the last impression you get from the chocolate, it receives equal importance in the overall rating.
    
    Overall Opinion is really where the ratings reflect a subjective opinion. Ideally it is my evaluation of whether or not the components above worked together and an opinion on the flavor development, character and style. It is also here where each chocolate can usually be summarized by the most prominent impressions that you would remember about each chocolate.
    
    Flavors of Cacao Rating System:
    5= Elite (Transcending beyond the ordinary limits)
    4= Premium (Superior flavor development, character and style)
    3= Satisfactory(3.0) to praiseworthy(3.75) (well made with special qualities)
    2= Disappointing (Passable but contains at least one significant flaw)
    1= Unpleasant (mostly unpalatable)

    Acknowledgements
    These ratings were compiled by Brady Brelinski, Founding Member of the Manhattan Chocolate Society. For up-to-date information, as well as additional content (including interviews with craft chocolate makers), please see his website: http://flavorsofcacao.com/index.html"""

desc = """Chocolate bar ratings."""
params = {
    'name': 'cacao_flavor',
    'description': desc,
    'creator': 'http://flavorsofcacao.com/index.html',
    'contributor': 'https://www.kaggle.com/rtatman/',
    'language': 'English',
    'licence': 'CC0 Public Domaine',
    'collection_date': '2017-08-12',
    'attributes': 'auto',
    'data': df,
    'ignore_attribute': None,
    'default_target_attribute': 'Bean Type',
    'row_id_attribute': df.index.name,
    'citation': None,
    'version_label': '0.1',
    'original_data_url': 'https://www.kaggle.com/rtatman/chocolate-bar-ratings/',
    'paper_url': None,
    'update_comment': None
}

dset = create_dataset(**params)
open_ml_id = dset.publish()
