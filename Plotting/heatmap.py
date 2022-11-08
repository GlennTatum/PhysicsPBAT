from mlxtend.plotting import heatmap
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import pandas as pd

df = pd.read_csv('savant_full_data.csv')

df.columns = ['hit_distance_sc', 'launch_speed', 'launch_angle']

cols = ['hit_distance_sc', 'launch_speed', 'launch_angle']

corrmat = np.corrcoef(df[cols].values.T)

fig, ax = heatmap(corrmat, column_names=cols, row_names=cols, cmap=cm.PiYG)

# set colorbar cutoff at -1, 1
for im in ax.get_images():
    im.set_clim(-1, 1)

plt.show()