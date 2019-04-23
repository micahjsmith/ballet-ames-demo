from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = "Open Porch SF"
transformer = SimpleFunctionTransformer(lambda ser: ser != 0)
name = "Has Open Porch"
feature = Feature(input=input, transformer=transformer, name=name)
