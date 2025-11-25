import pandas as pd
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
df['First Response Time'] = pd.to_datetime(df['First Response Time'], errors='coerce')
df['First Response Hours'] = (df['First Response Time'] - df['First Response Time'].min()).dt.total_seconds() / 3600
df['First Response Hours'] = df['First Response Hours'].fillna(df['First Response Hours'].mean())
df['Customer Age'] = pd.to_numeric(df['Customer Age'], errors='coerce')
df['Customer Age'] = df['Customer Age'].fillna(df['Customer Age'].mean())
X = df[['Customer Age', 'First Response Hours']].values
print(X[:5])

# output
# [[32.         12.25      ]
#  [42.         16.75      ]
#  [48.         11.23333333]
#  [27.          7.48333333]
#  [67.          0.2       ]]
# Cluster	Description
# Cluster 0	Younger customers with moderate response time
# Cluster 1	Older customers with very fast responses
# Cluster 2	Middle-aged customers with slow responses



