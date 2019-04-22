from ballet import Feature
from ballet.eng import NullFiller, SimpleFunctionTransformer

input = ["Yr Sold", "Year Remod/Add"]


def calc_age(df):
    return df["Yr Sold"] - df["Year Remod/Add"]


transformer = [SimpleFunctionTransformer(calc_age), NullFiller()]
name = "Age"
feature = Feature(input=input, transformer=transformer, name=name)
