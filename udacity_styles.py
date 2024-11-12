import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler
from matplotlib.patches import Patch, Circle

udacity_accent_colors = {
    "Light Blue": "#6597ff",
    # "Sky": "#6491fc",
    "Purple": "#b181ff",
    "Seafoam": "#00c5a1",
    "Lime": "#bdea09",
}

udacity_primary_colors = {
    "Black": "#0b0b0b",
    "Navy": "#171a53",
    "Brand Blue": "#2015ff",
    "White": "#ffffff"
}

udacity_transparent_colors = {
    "Transparent Light Blue": "#6597ff14",
    "Transparent Lime": "#bdea0914",
    "Transparent Purple": "#b181ff14",
    "Transparent Seafoam": "#00c5a114"
}

udacity_data_colors = {
    "Green": "#26a246",
    "Yellow": "#efc41c",
    "Orange": "#ff8329",
    "Red": "#e22c35"
}

udacity_extended_colors = udacity_accent_colors | {"Brand Blue": "#2015ff"} | \
                       udacity_data_colors

# line width in points
mpl.rcParams['lines.linewidth'] = 2
# edge line width
mpl.rcParams['axes.linewidth'] = 2
# colors for line plots
mpl.rcParams['axes.prop_cycle'] = cycler('color', udacity_extended_colors.values())
# figure face color
mpl.rcParams['figure.facecolor'] = 'none'
# axes edge color
mpl.rcParams['axes.facecolor'] = 'none'
# figure edge color
mpl.rcParams['figure.edgecolor'] = 'none'

# Customize spines to show only the bottom and left
mpl.rcParams['axes.spines.top'] = False
mpl.rcParams['axes.spines.right'] = False
mpl.rcParams['axes.spines.bottom'] = True
mpl.rcParams['axes.spines.left'] = True

# Set the tick length and width
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams["ytick.major.width"] = 2

# Hide the x-axis ticks because that's what the exemplar does
mpl.rcParams['xtick.color'] = "#ffffff00"
mpl.rcParams['xtick.labelcolor'] = udacity_primary_colors["Black"]

# Set the tick label font size
mpl.rcParams['xtick.labelsize'] = 18
mpl.rcParams['ytick.labelsize'] = 18

mpl.rcParams["axes.labelsize"] = 22
mpl.rcParams["font.size"] = 14
mpl.rcParams["axes.titlesize"] = 26
#mpl.rcParams["font.sans-serif"] = ["Open Sans"]

# Default width of the bar edges
mpl.rcParams['patch.linewidth'] = 0.5
mpl.rcParams['patch.edgecolor'] = udacity_primary_colors["Navy"]
mpl.rcParams["patch.force_edgecolor"] = True

mpl.rcParams['lines.marker'] = 'o'   # Set the default marker style to 'o' (circle)
mpl.rcParams['lines.markersize'] = 12  # Set the default marker size
mpl.rcParams['lines.linewidth'] = 2   # Set the default line width
mpl.rcParams['lines.markerfacecolor'] = udacity_primary_colors["White"]
mpl.rcParams['lines.markeredgecolor'] = 'auto' #udacity_primary_colors["Navy"]
mpl.rcParams['lines.markeredgewidth'] = 2

mpl.rcParams['grid.linewidth'] = 0.5
mpl.rcParams['grid.color'] = udacity_primary_colors["Black"]
# Enable minor ticks by default and set their length to 0 - we are only doing this for the grid
mpl.rcParams['xtick.minor.visible'] = True  # Turn on minor ticks for x-axis
mpl.rcParams['ytick.minor.visible'] = True  # Turn on minor ticks for y-axis
mpl.rcParams['xtick.minor.size'] = 0        # Set the minor tick length to 0 (x-axis)
mpl.rcParams['ytick.minor.size'] = 0