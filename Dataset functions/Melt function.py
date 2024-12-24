# Using melt() function 
import pandas as pd 
# Creating the DataFrame 
df1 = {"Name": ["Ravi", "Aniket", "Ana"], "ID": [1, 2, 3], "Role": 
["CEO", "Editor", "Author"]} 
df = pd.DataFrame(df1) 
# Printing the original DataFrame 
print(df) 
# Melting the DataFrame 
df_melted = pd.melt(df, id_vars=["ID"], value_vars=["Name", "Role"]) 
# Printing the melted DataFrame 
print(df_melted)