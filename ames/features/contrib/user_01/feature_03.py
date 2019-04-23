from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Misc Feature"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Misc Housing Feature Type"
feature = Feature(input=input, transformer=transformer, name=name)
