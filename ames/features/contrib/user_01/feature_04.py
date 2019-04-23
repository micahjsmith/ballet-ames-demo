from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Alley"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Alley Type"
feature = Feature(input=input, transformer=transformer, name=name)
