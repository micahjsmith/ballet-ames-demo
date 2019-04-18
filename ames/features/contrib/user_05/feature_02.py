from ballet import Feature
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

input = ["MS Zoning"]
transformer = [SimpleImputer(strategy="most_frequent"), OneHotEncoder()]
name = "MS Zoning Fill"
feature = Feature(input=input, transformer=transformer, name=name)
