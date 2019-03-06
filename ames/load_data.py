import pandas as pd


def load_data(input_dir=None):
    """Loads the Ames Housing dataset

    Source:

        Decock, Dean. "Ames, Iowa: Alternative to the Boston Housing Data as an
        End of Semester Regression Project."
        <https://ww2.amstat.org/publications/jse/v19n3/decock.pdf>
    """
    source = 'https://s3.amazonaws.com/mit-dai-ballet/ames/AmesHousing.txt'
    df = pd.read_table(source)
    X = df.drop('SalePrice', axis=1)
    y = df['SalePrice']
    return X, y

