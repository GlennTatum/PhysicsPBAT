from mlxtend.plotting import heatmap
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

df = pd.read_csv('savant_full_data.csv')

df.columns = ['hit_distance_sc', 'launch_speed', 'launch_angle']

cols = ['hit_distance_sc', 'launch_speed', 'launch_angle']

x = df['launch_speed'].values.T

y = df['hit_distance_sc'].values.T

plt.bar(x, y, alpha=0.5)


plt.show()