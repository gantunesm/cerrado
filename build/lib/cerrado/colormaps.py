
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors
import matplotlib
from cycler import cycler

PWD = os.path.dirname(os.path.abspath(__file__))


class ColorPalletSubset(pd.DataFrame):
    r"""
    """
    def _repr_html_(self):
        return f'{self.style.applymap(self._color_cell)._repr_html_()}<br>\n'

    @staticmethod
    def _color_cell(val):
        return f"color: {val}"

    def __getitem__(self, key):
        return self.iloc[0][key]


class ColorPallet:
    r"""Class to represent color pallets."""

    def __init__(self, ncolors=6):
        r"""Initialize function

        Parameters
        ----------
        ncolors: int
            The numbers of colors in the pallet
        """
        self.ncolors = ncolors
        self.colors = pd.read_csv(f'{PWD}/data/pallets/{ncolors}colors.csv',
                                  index_col=0)

    def __repr__(self):
        return self.colors.__repr__()

    def _repr_html_(self):
        return (f'<h3>Color Pallets with {self.ncolors} colors</h3>'
                f'{self.colors.style.applymap(self._color_cell)._repr_html_()}<br>\n')

    @staticmethod
    def _color_cell(val):
        return f"color: {val}"

    def view_all_colors(self):
        r"""Plot all colormaps in pallet."""
        for col, _ in self.colors.iterrows():
            self.view_colormap(col)

    def get_colors(self, colorid):
        r"""Select the cmap based on the id.

        Parameters
        ----------
        colorid: str
            the color pallet identifier

        Returns
        -------
        list of colors in the pallet
        """
        col = self.colors.loc[colorid].to_frame().T
        return ColorPalletSubset(col)

    def get_colormap(self, colorid):
        r"""Select the cmap based on the id.

        Parameters
        ----------
        colorid: str
            the color pallet identifier

        Returns
        -------
        matplotlib cmap object
        """
        col = self.colors.loc[colorid]
        cmap = matplotlib.colors.LinearSegmentedColormap.from_list("cerrado", col)
        return cmap

    def view_colormap(self, cmap, wspace=0, right=0.99,
                      top=0.99, bottom=0.00, left=0.01, hspace=0.0):
        r"""Plot colormap.

        Parameters
        ----------
        cmap: str or matplotlib.colors.cmap object
            the color pallet identifier or the cmap object

        Returns
        -------
        list of colors in the pallet
        """
        title = 'Color Map'
        if isinstance(cmap, str):
            title = cmap
            cmap = self.get_colormap(cmap)
        fig, _ = plt.subplots(figsize=(8, 0.5), dpi=100, sharey=True)
        fig.subplots_adjust(wspace=wspace, right=right, top=top, bottom=bottom,
                            left=left, hspace=hspace)
        plt.yticks([])
        arr = np.tile(np.arange(1000), 100).reshape(100, 1000)
        plt.title(title)
        plt.imshow(arr, cmap=cmap)

    def set_color_cycle(self, colorid):
        r"""Set matplotlib color cycler to colorid."""
        colors = self.get_colors(colorid)
        matplotlib.rcParams['axes.prop_cycle'] = cycler('color', colors.iloc[0])

    def set_colormap(self, colorid):
        r"""Set matplotlib colormap cycler to colorid."""
        cmap = self.get_colormap(colorid)
        plt.register_cmap(cmap=cmap)
        matplotlib.rcParams['image.cmap'] = 'cerrado'

    def set_color(self, colorid):
        r"""Set matplotlib color cycler and colormap to colorid."""
        self.set_color_cycle(colorid)
        self.set_colormap(colorid)
