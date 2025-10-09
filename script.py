from astroquery.gaia import Gaia
import pandas as pd

job = Gaia.launch_job_async("""
SELECT source_id, ra, dec, phot_g_mean_mag, parallax, pmra, pmdec
FROM gaiadr3.gaia_source
WHERE phot_g_mean_mag < 8
AND parallax > 0.1
AND ABS(b) < 30
""")

gaia_tbl = job.get_results()

print(gaia_tbl[:5])
