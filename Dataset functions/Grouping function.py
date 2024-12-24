# Grouping data 
import pandas as pd 
# Sample data 
punepl_data = { 
'Team': ['Warriors', 'Fighters', 'Supers', 'Fighters', 'Warriors', 
'Fighters', 'Fighters', 'Supers', 'Supers', 'Fighters', 'Warriors', 'Supers'], 
'Rank': [1, 2, 2, 3, 3, 4, 1, 1, 2, 4, 1, 2], 
'Year': [2004, 2005, 2004, 2005, 2004, 2005, 2006, 2007, 2006, 2004, 2005, 2007], 
'Points': [876, 789, 863, 673, 741, 812, 756, 788, 694, 701, 804, 690] 
} 
# Create DataFrame 
df = pd.DataFrame(punepl_data) 
print(df) 
# Print groups by Team 
print(df.groupby('Team').groups) 
# Iterating through groups by Year 
grouped = df.groupby('Year') 
for name, group in grouped: 
    print(name) 
    print(group) 
# Applying grouping and then applying aggregate function
grouped = df.groupby('Year') 
print(grouped['Points'].agg('mean'))  # Use string 'mean' instead of np.mean 
# Applying multiple aggregate functions 
grouped = df.groupby('Team') 
print(grouped['Points'].agg(['sum', 'mean', 'std']))  # Strings for aggregation functions 
# Applying filtration 
# Filter condition to return the teams which have participated four or more times in IPL 
print(df.groupby('Team').filter(lambda x: len(x) >= 4)) 