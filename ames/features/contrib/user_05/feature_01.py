import pandas as pd
from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Alley"]
transformer = [NullFiller(replacement="NOACCESS", isnull=pd.isnull), OneHotEncoder()]
name = "Alley Misc Fill"
feature = Feature(input=input, transformer=transformer, name=name)
