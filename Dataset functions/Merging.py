# Using the merge function 
import pandas as pd 
# First DataFrame 
left = pd.DataFrame({ 
"key": ["K0", "K1", "K2", "K3"], 
"A": ["A0", "A1", "A2", "A3"], 
"B": ["B0", "B1", "B2", "B3"], 
}) 
# Second DataFrame 
right = pd.DataFrame({ 
"key": ["K0", "K1", "K2", "K3"], 
"C": ["C0", "C1", "C2", "C3"], 
"D": ["D0", "D1", "D2", "D3"], 
}) 
# Merging the DataFrames 
result = pd.merge(left, right, on="key") 
# Printing the result 
print(result) 