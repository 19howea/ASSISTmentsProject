# list
a = [1,2,3]
# List cannot perform mathematical expression
# e.g: [1,2,3] + [4,5,6] =>>>> [1,2,3,4,5,6]

# tuple
b = (1,2,3)

# dictionary
c = {"Andrew": 20, "Dog": 156}

# numpy
import numpy as np
d = np.array([1,3,4,56])
e = np.array([1,23,4,10])

f = d + e

f

# pandas

import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
df.head()