from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = ["Overall Qual", "Overall Cond"]


def calc_qual(df):
    return df["Overall Qual"] - df["Overall Cond"]


transformer = SimpleFunctionTransformer(calc_qual)
name = "Qual"
feature = Feature(input=input, transformer=transformer, name=name)
