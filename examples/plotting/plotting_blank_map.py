"""
=============================
Plot positions on a blank map
=============================

This example showcases how to plot positions on a blank map.
It is commonly seen in papers and presentations to show HPC positions of events that occurred at
different times and therefore no single observation is appropriate.
"""

import matplotlib.pyplot as plt
import numpy as np

import sunpy.map
from sunpy.coordinates import frames

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits

################################################################################
# First we will create a blank map using with an array of zeros.
# Since there is no WCS information, we will need to construct a header to pass to Map.
data = np.full((1000, 1000), 0)

# Define coordinates and frame of reference and make the header using sunpy.map.make_fitswcs_header
skycoord = SkyCoord(0*u.arcsec, 0*u.arcsec, obstime='2013-10-28',
                    observer='earth', frame=frames.Helioprojective)
# Scale set to the following for solar limb to be in the field of view
header = sunpy.map.make_fitswcs_header(data, skycoord, scale=[2,2]*u.arcsec/u.pixel)

# Use sunpy.map.Map to create the blank map
blank_map = sunpy.map.Map(data, header)

################################################################################
# Now we have constructed the map, we can plot it and mark important locations to it.

# Initialize the plot and add the map to it
fig = plt.figure()
ax = plt.subplot(projection=blank_map)
blank_map.plot(alpha=0)
blank_map.draw_limb(color="k")
blank_map.draw_grid(color="k")

# Prevent the image from being re-scaled while overplotting.
ax.set_autoscale_on(False)

# Coordinates that are being plotted - (0, 0), (50, 100) and (400, 400)
xc = [0, 50, 400] * u.arcsec
yc = [0, 100, 400] * u.arcsec

# Place and mark coordinates on the plot
coords = SkyCoord(xc, yc, frame=blank_map.coordinate_frame)
p = ax.plot_coord(coords, 'o')

# Set title
ax.set_title('Plotting random points on a blank map')

# Display the plot
plt.show()
