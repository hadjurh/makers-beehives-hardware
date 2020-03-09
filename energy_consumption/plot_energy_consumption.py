import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import datetime
from glob import glob

helvetica_bold = fm.FontProperties(fname='C:/Users/hhadjur/Documents/Perso/asgbot/data/fonts/HelveticaNeueBold.ttf')
helvetica = fm.FontProperties(fname='C:/Users/hhadjur/Documents/Perso/asgbot/data/fonts/Helvetica-Normal.ttf')

out_files = glob('energy_consumption/output/*.out')

for out_file in out_files:
    task_name = out_file.split('\\')[-1].split('.out')[0]

    # Data
    df = pd.read_csv(out_file)
    df['timestamp'] = df['time'].apply(lambda t: datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f").timestamp())

    # Plot
    fig = plt.figure(figsize=(15, 7))
    ax = fig.add_subplot(111)
    axes_labels_font = helvetica_bold
    axes_labels_font.set_size(25)

    ax.step(df['timestamp'], df['current'], color='#007aff', linewidth=3, where='post', zorder=6)

    plt.ylim(0, 750)
    plt.xlabel('Time', fontproperties=helvetica_bold)
    plt.ylabel('Intensity (mA)', fontproperties=helvetica_bold)
    plt.title(f'Intensity evolution for: {task_name}', fontproperties=helvetica_bold, pad=20)
    for label in ax.get_yticklabels() + ax.get_xticklabels():
        label.set_fontproperties(axes_labels_font)

    fig.savefig(f'energy_consumption/plot/{task_name}_consumption.png', dpi=200)
    plt.close(fig)
