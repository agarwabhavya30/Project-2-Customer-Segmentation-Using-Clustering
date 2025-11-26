import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
df=pd.read_csv("C:\customers.csv",encoding="latin-1") 
df['First Response Time'] = pd.to_datetime(df['First Response Time'], errors='coerce') 
df['First Response Hours'] = (df['First Response Time'] - df['First Response Time'].min()).dt.total_seconds() / 3600 
df['First Response Hours'] = df['First Response Hours'].fillna(df['First Response Hours'].mean()) 
X = df[['Customer Age', 'First Response Hours']] 
# Elbow method 
inertialist = [] 
for k in range(1, 11): 
    kmeans = KMeans(n_clusters=k, random_state=42) 
    kmeans.fit(X) 
    inertialist.append(kmeans.inertia_) 
# Plotting the Elbow curve 
plt.plot(range(1, 11), inertialist, marker='o') 
plt.xlabel("Number of Clusters (K)") 
plt.ylabel("Inertia (WCSS)")
plt.title("Elbow Method") 
plt.show()