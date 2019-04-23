from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = ["Garage Yr Blt", "Year Built"]


def fill_garage(df):
    new_garage = df["Garage Yr Blt"].copy()
    mask = new_garage.isnull()
    new_garage[mask] = df["Year Built"][mask]
    return new_garage


transformer = SimpleFunctionTransformer(fill_garage)
name = "Impute garage year built"
feature = Feature(input=input, transformer=transformer, name=name)
