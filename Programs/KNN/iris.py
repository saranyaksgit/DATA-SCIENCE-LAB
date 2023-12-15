import csv
import numpy as np
import pandas as pd

dataset=pd.read_csv("Iris.csv")
print(dataset)
print("\n\n",dataset.shape)
print("\n\n",dataset.head(5))

X=dataset.iloc[:,:-1]
print("\n\n",X)

Y=dataset.iloc[:,-1].values
print("\n\n",Y)
