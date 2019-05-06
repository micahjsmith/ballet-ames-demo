from ballet.util.io import load_table_from_config
from funcy import some, where

from ames import conf


def load_data(input_dir=None):
    """Load data"""
    if input_dir is not None:
        tables = conf.get('tables')

        entities_table_name = conf.get('data', 'entities_table_name')
        entities_config = some(where(tables, name=entities_table_name))
        X = load_table_from_config(input_dir, entities_config)

        targets_table_name = conf.get('data', 'targets_table_name')
        targets_config = some(where(tables, name=targets_table_name))
        y = load_table_from_config(input_dir, targets_config)
    else:
        raise NotImplementedError

    return X, y
