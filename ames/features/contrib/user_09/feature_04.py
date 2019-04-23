from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["BsmtFin Type 2"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Basement Finished Area Type 2 Fill"
feature = Feature(input=input, transformer=transformer, name=name)
