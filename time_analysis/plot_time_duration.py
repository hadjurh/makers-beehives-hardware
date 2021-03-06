import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

helvetica_bold = fm.FontProperties(fname='D:/Users/Hugo/Documents/asgbot/data/fonts/HelveticaNeueBold.ttf')
helvetica = fm.FontProperties(fname='D:/Users/Hugo/Documents/asgbot/data/fonts/Helvetica-Normal.ttf')

df = pd.read_csv('time_analysis/output/nb_img.out')

# Plot
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111)
axes_labels_font = helvetica_bold
axes_labels_font.set_size(25)
helvetica.set_size(20)

ax.scatter(df['nb_img'], df['duration'], color='#007aff', s=400, alpha=0.6, zorder=6)

# Linear Regression
regressor = LinearRegression()
regressor.fit(np.array(df['nb_img']).reshape(-1, 1), np.array(df['duration']).reshape(-1, 1))  # training the algorithm
r2 = regressor.score(np.array(df['nb_img']).reshape(-1, 1), np.array(df['duration']).reshape(-1, 1))

line_x = np.linspace(0, 50, 500)
line_y = [x * regressor.coef_[0][0] + regressor.intercept_[0] for x in line_x]
ax.plot(line_x, line_y)

plt.text(s=f'duration = {round(regressor.coef_[0][0], 3)} * pixels + '
           f'{round(regressor.intercept_[0], 3)}\n'
           f'R-squared = {round(r2, 4)}',
         x=3,
         y=23,
         fontproperties=helvetica
         )

plt.xlabel('Number of Images', fontproperties=helvetica_bold)
plt.ylabel('Duration of Capture', fontproperties=helvetica_bold)
helvetica_bold.set_size(30)
plt.title('Time to Capture Images with a PiCamera', fontproperties=helvetica_bold, pad=25)
for label in ax.get_yticklabels() + ax.get_xticklabels():
    label.set_fontproperties(axes_labels_font)

fig.savefig(f'time_analysis/plot/nb_img_time_no_sleep.png', dpi=200)
plt.close(fig)

