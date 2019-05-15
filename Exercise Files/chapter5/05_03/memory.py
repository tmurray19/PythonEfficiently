
import numpy as np

@profile
def allocator():
    vector_list = [float(i) for i in range(1000000)]
    vector_np = np.arange(0,1000000, dtype='d')

allocator()
