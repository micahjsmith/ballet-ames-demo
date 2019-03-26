from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Alley"]
transformer = [NullFiller(replacement="NOACCESS"), OneHotEncoder()]
name = "Alley Misc Fill"
feature = Feature(input=input, transformer=transformer, name=name)
