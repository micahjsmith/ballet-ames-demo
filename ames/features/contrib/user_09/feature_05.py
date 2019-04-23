from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = "BsmtFin SF 2"


def has_qual(df):
    return (df > 0).astype(int)


transformer = SimpleFunctionTransformer(has_qual)
name = "Basement Finished Area Type 2 Indicator"
feature = Feature(input=input, transformer=transformer, name=name)
