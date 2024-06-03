import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Paths to your data files
file_paths = [
    "/home/edwin/Downloads/samsung_s10.csv",
    "/home/edwin/Downloads/samsung_s21.csv",
    "/home/edwin/Downloads/Iphone15PROUSA.csv",
    "/home/edwin/Downloads/Computer.csv",
    "/home/edwin/Downloads/Lars_telefon.csv",
    
]

# Names for each dataset
dataset_names = ["Samsung S10", "Samsung S21", "iPhone 15 PRO", "Lenove Legion 5 Pro 16", "OnePlus Nord 3"]

cluster_score = []

# Load, cluster each file, filter outliers, and collect cleaned data
def load_cluster_filter(filepath, name):
    data = np.loadtxt(filepath, delimiter=',')
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # K-means with one cluster to find the central point
    kmeans = KMeans(n_clusters=1, init='k-means++', max_iter=300, n_init=10)
    kmeans.fit(data_scaled)
    center = kmeans.cluster_centers_[0]

    # Calculate distances from the center and filter
    distances = np.linalg.norm(data_scaled - center, axis=1)
    threshold = np.percentile(distances, 80)  # Remove the top 20% farthest points
    filtered_data = data[distances < threshold]

    return filtered_data, name

# Process each file and collect filtered data along with names
filtered_datasets = [load_cluster_filter(path, name) for path, name in zip(file_paths, dataset_names)]

# Concatenate all filtered data
merged_filtered_data = np.vstack([data for data, _ in filtered_datasets])
labels_data = np.concatenate([np.full(data.shape[0], name) for data, name in filtered_datasets])

# Save the merged, filtered data
output_file_path = '/home/edwin/Downloads/EMC2_data.csv'
np.savetxt(output_file_path, merged_filtered_data, delimiter=',')

# Functions for calculating WCSS and plotting
def calculate_wcss(data):
    wcss = []
    for n in range(1, 11):
        kmeans = KMeans(n_clusters=n, init='k-means++', n_init=10, max_iter=1000)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    return wcss

def plot_elbow(wcss):
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), wcss, 'o-')
    plt.title('Elbow Method')
    plt.xlabel('Number of clusters')
    plt.ylabel('WCSS')
    plt.show()

def perform_k_means(file_path, range_n_clusters=(2, 11)):
    data = np.loadtxt(file_path, delimiter=',')
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    wcss = calculate_wcss(data_scaled)
    plot_elbow(wcss)

    optimal_clusters_score = (0, 2)  # Default value to avoid referenced before assignment error
    for n_clusters in range(*range_n_clusters):
        clusterer = KMeans(n_clusters=n_clusters, init='k-means++', n_init=10, max_iter=300)
        preds = clusterer.fit_predict(data_scaled)
        score = silhouette_score(data_scaled, preds)
        cluster_score.append((score, n_clusters))
        print(f"Silhouette score for {n_clusters} clusters: {score}")

    optimal_clusters_score = max(cluster_score, key=lambda x: x[0])
    optimal_cluster_number = optimal_clusters_score[1]
    kmeans = KMeans(n_clusters=optimal_cluster_number, init='k-means++', n_init=10, max_iter=300)
    kmeans.fit(data_scaled)

    plt.figure(figsize=(8, 6))
    for label in np.unique(labels_data):
        subset = data_scaled[labels_data == label]
        plt.scatter(subset[:, 0], subset[:, 1], label=label)
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red', label='Centroids', marker='X')
    plt.title('K-Means Clustering')
    plt.legend()
    plt.show()

    return kmeans.cluster_centers_, kmeans.labels_

# Perform clustering on the combined, filtered dataset
centroids, labels = perform_k_means(output_file_path)

