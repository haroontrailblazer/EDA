import pandas as pd 
# Creating the DataFrame 
d1 = { "Name": ["Ravi", "Aniket", "Ana"], "ID": [1, 2, 3], "Role": 
["CEO", "Editor", "Author"] 
} 
df = pd.DataFrame(d1) 
# Printing the original DataFrame 
print(df) 
# Melting the DataFrame 
df_melted = pd.melt(df, id_vars=["ID"], value_vars=["Name", 
"Role"], var_name="Attribute", value_name="Value") 
print(df_melted) 
# Unmelting using pivot() 
df_unmelted = df_melted.pivot(index='ID', columns='Attribute', 
values='Value') 
print(df_unmelted) 