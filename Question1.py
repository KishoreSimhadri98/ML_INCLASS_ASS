import numpy as np
#1
arr=np.random.randint(1,20,15)
print("\nRandom vectors: ",arr,"\n")
arr2 = np.reshape(arr,(3,5))
print("Reshaped array: \n", arr2, "\n")
#2
print("Shape of the array: ", arr2.shape, "\n")
#3
arr3= np.max(arr2)
print("Max Element: ", arr3, "\n")
arr2[np.where(arr2==arr3)]=0
print("Array with max element 0: \n",arr2)



