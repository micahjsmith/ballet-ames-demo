from ballet import Feature
from ballet.eng import SimpleFunctionTransformer
from sklearn.preprocessing import OneHotEncoder

"""Zeros in 020-090 get cut off. This feature prepends them back."""

input = "MS SubClass"


def pad_zero(ser):
    ser.astype(str).str.pad(3, side="left", fillchar="0")


transformer = [SimpleFunctionTransformer(pad_zero), OneHotEncoder()]
name = "Pad zeros in MS SubClass"
feature = Feature(input=input, transformer=transformer, name=name)
