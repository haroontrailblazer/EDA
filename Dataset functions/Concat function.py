# Using concat function 
import pandas as pd 
# First DataFrame 
df1 = pd.DataFrame({ 
'id': ['T01', 'T02', 'T03', 'T04'], 
'Name': ['Jiya', 'Riya', 'Maya', 'Piya'] 
}) 
# Second DataFrame 
df2 = pd.DataFrame({ 
'id': ['R05', 'R06', 'R07', 'R08'], 
'Name': ['Raam', 'Raaj', 'Naaz', 'Saaj'] 
}) 
# List of DataFrames to concatenate 
frames = [df1, df2] 
# Concatenating the DataFrames 
result = pd.concat(frames) 
# Printing the result 
print(result)