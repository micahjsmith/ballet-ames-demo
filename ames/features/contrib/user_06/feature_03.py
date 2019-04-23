from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Garage Type"]
transformer = [NullFiller(replacement="Missing"), OneHotEncoder()]
name = "Garage Type Fill"
feature = Feature(input=input, transformer=transformer, name=name)
