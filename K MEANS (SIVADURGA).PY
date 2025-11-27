
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv("C:\customers.csv",encoding="latin-1")

# Converting 'First Response Time' to hours
df['First Response Time'] = pd.to_datetime(df['First Response Time'], errors='coerce')
df['First Response Hours'] = (df['First Response Time'] - df['First Response Time'].min()).dt.total_seconds() / 3600
df['First Response Hours'] = df['First Response Hours'].fillna(df['First Response Hours'].mean())

X = df[['Customer Age', 'First Response Hours']]
# Applying K-Means clustering 
k = 3 
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)
for i in range(k):
    cluster = df[df['Cluster'] == i]
    print("Cluster", i)
    print("Number of customers:", len(cluster))
    print("Average Response Time (hours):", round(cluster['First Response Hours'].mean()))

output
Cluster 0
Number of customers: 4261
Average Response Time (hours): 13
Cluster 1
Number of customers: 38
Average Response Time (hours): 744
Cluster 2
Number of customers: 4170
Average Response Time (hours): 14

