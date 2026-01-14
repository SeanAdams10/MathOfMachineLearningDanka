from sklearn.datasets import load_iris

data = load_iris()
print(data.data)
x, y = data['data'], data['target']
print(x[:10])