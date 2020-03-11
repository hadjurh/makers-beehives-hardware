import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from colour import Color
import csv
import ast


def plot_thermal(temp_array, file_name='test'):
    color_depth = 1024
    blue = Color("indigo")
    colors = list(blue.range_to(Color("red"), color_depth))
    colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

    sns.heatmap(
        np.reshape(ast.literal_eval(temp_array), (8, 8)),
        vmin=15, vmax=38,
        cmap=['#%02x%02x%02x' % c for c in colors],
        square=True
    )

    plt.gcf().savefig('img/' + file_name + '.png', dpi=200)

    plt.close()


if __name__ == '__main__':
    with open('out.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        for i, row in enumerate(spamreader):
            print(i)

            thermal_data = row[1]

            plot_thermal(thermal_data, 'img_' + str(i + 1))
