import cupy as cp
import numpy as np
  
x_cpu = np.array([1, 2, 3])
x_gpu = cp.array([1, 2, 3])
  
l2_cpu = np.linalg.norm(x_cpu)
l2_gpu = cp.linalg.norm(x_gpu)
  
print("Using Numpy: ", l2_cpu)
print("\nUsing Cupy: ", l2_gpu)