from .colormaps import ColorPallet
from .photo2colors import *
# view_colormap, view_all_colors, get_colors, \
#                        get_colormap, set_color_cycle, set_colormap, \
#                        set_color
import matplotlib.pyplot as plt
import os

PWD = os.path.dirname(os.path.abspath(__file__))
plt.style.use(f'{PWD}/data/styles/defaults.mplstyle')

pallet = ColorPallet(6)
pallet.set_color('chuveirinho')
