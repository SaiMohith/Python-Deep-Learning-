import numpy as np

array = np.random.randint(0, 20, size=15)
print(array)
counts = np.bincount(array)
print("Most Repeated Value:", np.argmax(counts))
