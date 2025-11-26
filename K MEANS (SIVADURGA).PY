import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df=pd.read_csv("C:\customers.csv",encoding="latin-1")
# Converting 'First Response Time' to hours
df['First Response Time'] = pd.to_datetime(df['First Response Time'], errors='coerce')
df['First Response Hours'] = (df['First Response Time'] - df['First Response Time'].min()).dt.total_seconds() / 3600
df['First Response Hours'] = df['First Response Hours'].fillna(df['First Response Hours'].mean())

df['Customer Age'] = pd.to_numeric(df['Customer Age'], errors='coerce')
df['Customer Age'] = df['Customer Age'].fillna(df['Customer Age'].mean())
X = df[['Customer Age', 'First Response Hours']]
# Applying K-Means clustering 
k = 3 
kmeans = KMeans(n_clusters=k, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)
# Plotting the clusters
plt.figure(figsize=(8,5))
colors = ['red', 'green', 'blue']
for i in range(k):
    cluster_points = df[df['Cluster'] == i]
    plt.scatter(cluster_points['Customer Age'], cluster_points['First Response Hours'], 
                c=colors[i], label=f'Cluster {i}', alpha=0.6)

# Plotting centroids
plt.xlabel('Customer Age')
plt.ylabel('First Response Time (hours)')
plt.title('K-Means Clustering: Age vs First Response Time')
plt.legend()
plt.grid(True)
plt.show()
# CLUSTER SUMMARY
for i in range(k):
    cluster_data = df[df['Cluster'] == i]
    print(f"\nCluster {i}:")
    print(f"Number of customers: {len(cluster_data)}")
    print(f"Average Age: {cluster_data['Customer Age'].mean():.2f}")
    print(f"Average First Response Time (hours): {cluster_data['First Response Hours'].mean():.2f}")

# output (cluster summary)
#     Cluster 0:
# Number of customers: 4261
# Average Age: 30.91
# Average First Response Time (hours): 13.46

# Cluster 1:
# Number of customers: 38
# Average Age: 45.13
# Average First Response Time (hours): 744.32

# Cluster 2:
# Number of customers: 4170
# Average Age: 57.42
# Average First Response Time (hours): 13.63