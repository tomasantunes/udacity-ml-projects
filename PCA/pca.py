from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pca.fit(data)

print(pca.explained_variance_ratio_)
first_pc = pca.components_[0]
second_pc = pca.components_[1]

tranformed_data = pca.transform(data)