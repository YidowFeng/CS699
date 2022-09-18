import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('a1.csv')
print(np.corrcoef(df['A1'].values, df['A5'].values))
print(np.corrcoef(df['A2'].values, df['A5'].values))
print(np.corrcoef(df['A3'].values, df['A5'].values))
print(np.corrcoef(df['A4'].values, df['A5'].values))

plt.scatter(df['A1'].values, df['A5'].values)
plt.show()
plt.scatter(df['A2'].values, df['A5'].values)
plt.show()
plt.scatter(df['A3'].values, df['A5'].values)
plt.show()
plt.scatter(df['A4'].values, df['A5'].values)
plt.show()