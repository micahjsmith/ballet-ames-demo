from ballet import Feature
from sklearn.impute import SimpleImputer

# BsmtFinSF1, BsmtFinSF2, BsmtUnfSF, TotalBsmtSF, BsmtFullBath and BsmtHalfBath :
# missing values are likely zero for having no basement

input = ["Total Bsmt SF"]
transformer = SimpleImputer(strategy="mean")
name = "Total Basement Area Fill"
feature = Feature(input=input, transformer=transformer)
