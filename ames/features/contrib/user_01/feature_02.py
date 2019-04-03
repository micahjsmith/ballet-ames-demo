from ballet import Feature
from ballet.eng.missing import NullFiller
from sklearn.preprocessing import OneHotEncoder

# PoolQC : data description says NA means "No Pool".
# That make sense, given the huge ratio of missing value (+99%)
# and majority of houses have no Pool at all in general.
input = ["Pool QC"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Pool Type"
feature = Feature(input=input, transformer=transformer, name=name)
