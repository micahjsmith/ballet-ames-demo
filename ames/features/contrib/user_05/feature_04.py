from ballet import Feature
from sklearn.impute import SimpleImputer

input = ["Lot Frontage"]
transformer = SimpleImputer(strategy="mean")
name = "Lot Frontage Fill"
feature = Feature(input=input, transformer=transformer, name=name)
