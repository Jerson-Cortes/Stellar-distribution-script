
# Here we convert values from equatorial to cartesian.

import pandas as pd

from astropy import units as u
from astropy.coordinates import SkyCoord

df = pd.read_csv("data/bright_gaia_stars_raw.csv")

df['pc'] = 1000.0/df['parallax']

coord = SkyCoord(ra=df['ra'], dec=df['dec'], distance=df['pc']*u.pc, unit=(u.degree, u.degree))
df['x'] = coord.cartesian.x.value
df['y'] = coord.cartesian.y.value
df['z'] = coord.cartesian.z.value

df.to_csv('data/bright_gaia_stars.csv', index=False)
