import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from colour import Color


def plot_thermal(temp_array):
    color_depth = 1024
    blue = Color("indigo")
    colors = list(blue.range_to(Color("red"), color_depth))
    colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

    sns.heatmap(
        np.reshape(temp_array, (8, 8)),
        cmap=['#%02x%02x%02x' % c for c in colors],
        square=True
    )

    plt.gcf().savefig('test.png', dpi=200)
