import numpy as np
np.random.seed(0)

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class KMeans:
    def __init__(self, K=5, max_iters=100, plot_steps=False):
        self.K = K
        self.max_iters = max_iters
        self.plot_steps = plot_steps
        self.clusters = [[] for _ in range(self.K)]
        self.centroids = []
 
    def _create_clusters(self, centroids):
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            distances = [euclidean_distance(sample, point) for point in centroids]
            closest_index = np.argmin(distances)
            centroid_idx = closest_index
            clusters[centroid_idx].append(idx)
        return clusters
 
    def predict(self, X):
        self.X = X
        self.n_samples, self.n_features = X.shape
 
        random_sample_idxs = np.random.choice(self.n_samples, self.K, replace=False)
        self.centroids = [self.X[idx] for idx in random_sample_idxs]
 
        for _ in range(self.max_iters):
            self.clusters = self._create_clusters(self.centroids)
 
            centroids_old = self.centroids
            self.centroids = self.get_new_centroids(self.clusters)
            if self._is_converged(centroids_old, self.centroids):
                print('stop at', _)
                break
            if self.plot_steps:
                self.plot()
        return self.clusters
 
    def get_new_centroids(self, clusters):
        centroids = np.zeros((self.K, self.n_features))
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = np.mean(self.X[cluster], axis=0)
            centroids[cluster_idx] = cluster_mean
        return centroids
 
    def _is_converged(self, centroids_old, centroids):
        distances = [
            euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.K)
        ]
        return sum(distances) == 0

Point = []
Point.append([0, 4, 1])
Point.append([4, 1, 0])
Point.append([3, 2, 0])
Point.append([2, 3, 2])
Point.append([2, 4, 1])
Point.append([2, 3, 4])
Point = np.asarray(Point)
k = KMeans(K=3, max_iters=100, plot_steps=False)
y_pred = k.predict(Point)
print(y_pred)
for index, value in enumerate(y_pred):
    print("Cluster:", index+1)
    for v in value:
        print(Point[v])
print("Centroids:", k.centroids)
