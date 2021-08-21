from .colormaps import view_colormap, view_all_colors, get_colors, \
                       get_colormap, set_color_cycle, set_colormap, \
                       set_color
import matplotlib.pyplot as plt
import os

PWD = os.path.dirname(os.path.abspath(__file__))
plt.style.use(f'{PWD}/data/styles/defaults.mplstyle')

set_color('cer1', npallet=6)
