import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('a2-p2.csv')
print("correl(A1, A4)")
print(np.corrcoef(df['A1'].values, df['A4'].values))
print("correl(A2, A4)")
print(np.corrcoef(df['A2'].values, df['A4'].values))
print("correl(A3, A4)")
print(np.corrcoef(df['A3'].values, df['A4'].values))

