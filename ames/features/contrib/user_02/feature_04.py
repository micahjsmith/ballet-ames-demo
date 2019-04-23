from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Heating"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Heating Type"
feature = Feature(input=input, transformer=transformer, name=name)
