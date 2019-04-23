from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["MS SubClass"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "MS Fill None"
feature = Feature(input=input, transformer=transformer, name=name)
