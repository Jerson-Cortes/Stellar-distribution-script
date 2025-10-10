
#This script is isoleted from the rest due to some problems I had when trying to run it. The problem in all likelihood arose on the account of rate limits.

from astroquery.gaia import Gaia
import pandas as pd

job = Gaia.launch_job_async("""
SELECT source_id, ra, dec, phot_g_mean_mag, parallax, pmra, pmdec
FROM gaiadr3.gaia_source
WHERE phot_g_mean_mag > 8
AND parallax > 0.1
AND ABS(b) < 30
""")

gaia_tbl = job.get_results()

df = gaia_tbl.to_pandas()
df.to_csv('bright_gaia_stars_raw.csv', index=False)
