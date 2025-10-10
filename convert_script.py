
# Here we convert values from equatorial to cartesian.

import pandas as pd

from astropy import units as u
from astropy.coordinates import SkyCoord

df = pd.read_csv("data/bright_gaia_stars_raw.csv")

df['pc'] = 1000.0/df['parallax']

new_df = pd.DataFrame()

coord = SkyCoord(ra=df['ra'], dec=df['dec'], distance=new_df['pc']*u.pc, unit=(u.degree, u.degree))
new_df['x'] = coord.cartesian.x.value
new_df['y'] = coord.cartesian.y.value
new_df['z'] = coord.cartesian.z.value

new_df.to_csv('data/bright_gaia_stars1.csv', index=False)
