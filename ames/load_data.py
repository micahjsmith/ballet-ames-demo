import pandas as pd
from ballet.util.io import load_table_from_config
from funcy import some, where

from ames import conf


def load_data(input_dir=None):
    """Loads the Ames Housing dataset

    Source:

        Decock, Dean. "Ames, Iowa: Alternative to the Boston Housing Data as an
        End of Semester Regression Project."
        <https://ww2.amstat.org/publications/jse/v19n3/decock.pdf>
    """
    if input_dir is not None:
        tables = conf.get('tables')

        entities_table_name = conf.get('data', 'entities_table_name')
        entities_config = some(where(tables, name=entities_table_name))
        X = load_table_from_config(input_dir, entities_config)

        targets_table_name = conf.get('data', 'targets_table_name')
        targets_config = some(where(tables, name=targets_table_name))
        y = load_table_from_config(input_dir, targets_config)
    else:
        source = 'https://s3.amazonaws.com/mit-dai-ballet/ames/AmesHousing.txt'
        df = pd.read_csv(source, sep='\t')
        X = df.drop('SalePrice', axis=1)
        y = df['SalePrice']

    return X, y
