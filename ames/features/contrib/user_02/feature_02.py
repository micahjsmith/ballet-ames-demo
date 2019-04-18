from ballet import Feature
from sklearn.preprocessing import OneHotEncoder


input = ["Mo Sold"]
transformer = OneHotEncoder()
name = "Month Sold Categorical"
feature = Feature(input=input, transformer=transformer, name=name)
