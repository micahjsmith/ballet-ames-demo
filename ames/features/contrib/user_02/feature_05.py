from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Foundation"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Foundation Type"
feature = Feature(input=input, transformer=transformer, name=name)
