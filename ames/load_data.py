import pandas as pd
from ballet.compat import pathlib
from ballet.util import one_or_raise
from ballet.util.io import load_table_from_config
from funcy import lwhere
from sklearn.model_selection import train_test_split

from ames import conf


def load_data(input_dir=None):
    """Loads the Ames Housing dataset

    Source::

        Decock, Dean. "Ames, Iowa: Alternative to the Boston Housing Data as an
        End of Semester Regression Project."
        <https://ww2.amstat.org/publications/jse/v19n3/decock.pdf>
        <https://s3.amazonaws.com/mit-dai-ballet/ames/DataDocumentation.txt >
    """
    if input_dir is not None:
        tables = conf.get('tables')

        entities_table_name = conf.get('data', 'entities_table_name')
        entities_config = one_or_raise(lwhere(tables, name=entities_table_name))
        X_df = load_table_from_config(input_dir, entities_config)

        targets_table_name = conf.get('data', 'targets_table_name')
        targets_config = one_or_raise(lwhere(tables, name=targets_table_name))
        y_df = load_table_from_config(input_dir, targets_config)
    else:
        source = 'https://s3.amazonaws.com/mit-dai-ballet/ames/AmesHousing.txt'
        df = pd.read_csv(source, sep='\t')
        X_df = df.drop('SalePrice', axis=1)
        y_df = df['SalePrice']

    return X_df, y_df


def make_train_test_split(output_dir, seed=641137):
    # load and split data
    X, y = load_data()
    inds = X.index.copy()
    inds_tr, inds_te = train_test_split(inds,
                                        train_size=0.67,
                                        test_size=0.33,
                                        random_state=seed)
    X_tr_df = X.loc[inds_tr]
    X_te_df = X.loc[inds_te]
    y_tr_df = y.loc[inds_tr]
    y_te_df = y.loc[inds_te]

    # load config
    tables = conf.get('tables')
    entities_table_name = conf.get('data', 'entities_table_name')
    entities_config = one_or_raise(lwhere(tables, name=entities_table_name))
    entities_path = entities_config['path']
    targets_table_name = conf.get('data', 'targets_table_name')
    targets_config = one_or_raise(lwhere(tables, name=targets_table_name))
    targets_path = targets_config['path']

    # prepare directories
    output_dir = pathlib.Path(output_dir)
    train_dir = output_dir.joinpath('train')
    train_dir.mkdir(exist_ok=True)
    test_dir = output_dir.joinpath('test')
    test_dir.mkdir(exist_ok=True)

    # save tables
    kwargs = {'header': True}
    X_tr_df.to_csv(train_dir.joinpath(entities_path), **kwargs)
    X_te_df.to_csv(test_dir.joinpath(entities_path), **kwargs)
    y_tr_df.to_csv(train_dir.joinpath(targets_path), **kwargs)
    y_te_df.to_csv(test_dir.joinpath(targets_path), **kwargs)

    return X_tr_df, X_te_df, y_tr_df, y_te_df
