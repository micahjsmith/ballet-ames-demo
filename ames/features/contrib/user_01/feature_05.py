from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Fence"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Fence Type"
feature = Feature(input=input, transformer=transformer, name=name)
