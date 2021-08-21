
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib
from cycler import cycler

PWD = os.path.dirname(os.path.abspath(__file__))


def view_all_colors(npallet=6):
    r"""Plot all colormaps in pallet.

    Parameter
    ---------
    npallet: int
        The number of colors in the pallet
    """
    colors = pd.read_csv(f'{PWD}/data/pallets/{npallet}colors.csv',
                         index_col=0)
    for col, _ in colors.iterrows():
        view_colormap(col)


def get_colors(colorid, npallet=6):
    r"""Select the cmap based on the id.

    Parameters
    ----------
    colorid: str
        the color pallet identifier

    npallet: int
        The number of colors in the pallet

    Returns
    -------
    list of colors in the pallet
    """
    colors = pd.read_csv(f'{PWD}/data/pallets/{npallet}colors.csv',
                         index_col=0)
    col = colors.loc[colorid]
    return col

def get_colormap(colorid, npallet=6):
    r"""Select the cmap based on the id.

    Parameters
    ----------
    colorid: str
        the color pallet identifier

    npallet: int
        The number of colors in the pallet

    Returns
    -------
    matplotlib cmap object
    """
    colors = pd.read_csv(f'{PWD}/data/pallets/{npallet}colors.csv',
                         index_col=0)
    col = colors.loc[colorid]
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list("cerrado", col)
    return cmap


def view_colormap(cmap, npallet=6):
    r"""Plot colormap.

    Parameters
    ----------
    cmap: str or matplotlib.colors.cmap object
        the color pallet identifier or the cmap object

    npallet: int
        The number of colors in the pallet

    Returns
    -------
    list of colors in the pallet
    """
    title = 'Color Map'
    if isinstance(cmap, str):
        title = cmap
        cmap = get_colormap(cmap, npallet=npallet)
    f, axes = plt.subplots(figsize=(8, 0.5), dpi=100, sharey=True)
    f.subplots_adjust(wspace=0,right=0.99,top=0.99,bottom=0.00,left=0.01,hspace=0.0)
    plt.yticks([])
    arr=np.tile(np.arange(1000),100).reshape(100,1000)
    plt.title(title)
    plt.imshow(arr,cmap=cmap)


def set_color_cycle(colorid, npallet=6):
    r"""
    """
    colors = get_colors(colorid, npallet=npallet)
    matplotlib.rcParams['axes.prop_cycle'] = cycler('color', colors)


def set_colormap(colorid, npallet=6):
    r"""
    """
    cmap = get_colormap(colorid, npallet=npallet)
    plt.register_cmap(cmap=cmap)
    matplotlib.rcParams['image.cmap'] = 'cerrado'


def set_color(colorid, npallet=6):
    r"""
    """
    set_color_cycle(colorid)
    set_colormap(colorid)
