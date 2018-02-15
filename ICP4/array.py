import numpy as np
arr=np.random.random_integers(100,size=(10,10))
print(arr)
maxrow= arr.max(axis=1)
minrow=arr.min(axis=1)
print("max number in each row are:", maxrow)
print("min number in each row are:", minrow)