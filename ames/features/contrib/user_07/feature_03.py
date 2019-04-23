from ballet import Feature
from sklearn.impute import SimpleImputer

# BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF, BsmtFullBath and BsmtHalfBath :
# missing values are likely zero for having no basement

input = ["Bsmt Unf SF"]
transformer = SimpleImputer(strategy="mean")
name = "Basement Unfinished Area Fill"
feature = Feature(input=input, transformer=transformer, name=name)
