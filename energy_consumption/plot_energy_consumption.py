import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import datetime
from glob import glob

helvetica_bold = fm.FontProperties(fname='D:/Users/Hugo/Documents/asgbot/data/fonts/HelveticaNeueBold.ttf')
helvetica = fm.FontProperties(fname='D:/Users/Hugo/Documents/asgbot/data/fonts/Helvetica-Normal.ttf')

out_files = glob('energy_consumption/output/*.out')

for out_file in out_files:
    # Plot
    fig = plt.figure(figsize=(21, 7))
    ax = fig.add_subplot(111)
    axes_labels_font = helvetica_bold
    axes_labels_font.set_size(25)
    print(out_file)
    # Only git pull
    # if 'compare_img_size_v2.out' not in out_file:
    #     continue

    task_name = out_file.split('\\')[-1].split('.out')[0]

    # Data
    df = pd.read_csv(out_file)
    df['timestamp'] = df['time'].apply(lambda t: datetime.datetime.strptime(t, "%Y-%m-%d %H:%M:%S.%f").timestamp())
    df['timestamp'] = df['timestamp'] - min(df['timestamp'])
    print(df['current'].mean())

    ax.step(df['timestamp'], df['current'] * 5 / 1000, linewidth=2, where='post', zorder=6)

    # plt.ylim(230 * 5 / 1000, 390 * 5 / 1000)
    plt.xlabel('Time', fontproperties=helvetica_bold)
    plt.ylabel('Power (W)', fontproperties=helvetica_bold)
    plt.title(f'Power evolution for: {task_name}', fontproperties=helvetica_bold, pad=20)
    for label in ax.get_yticklabels() + ax.get_xticklabels():
        label.set_fontproperties(axes_labels_font)

    fig.savefig(f'energy_consumption/plot/{task_name}_power_consumption.png', dpi=200)
    plt.close(fig)

