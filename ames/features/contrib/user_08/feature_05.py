from ballet import Feature
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

input = ["Electrical"]
transformer = [SimpleImputer(strategy="mean"), OneHotEncoder()]
name = "Electrical Type Fill"
feature = Feature(input=input, transformer=transformer, name=name)
