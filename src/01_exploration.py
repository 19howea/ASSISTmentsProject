import pandas as pd
import numpy as np

#load dataset
df = pd.read_csv("/Users/andrewhowe/Documents/Phong_PCLA/ASSISTmentProject/Dataset/2012-2013-data-with-predictions-4-final.csv",
                 low_memory=False)
df_small = df.sample(100000)
df_small.to_csv("/Users/andrewhowe/Documents/Phong_PCLA/ASSISTmentProject/Dataset/2012-2013-data-with-predictions-4-final-small.csv")

# Quick info of the dataset
df.info()

# Check for missing data
df.isnull().sum()

# Check for some stats
df.describe()