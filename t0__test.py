from datetime import datetime

import humanize

d1 = datetime.now()

d2 = datetime.now().replace(hour=2, minute=32)
delta = d2 - d1
res = humanize.naturaldelta(delta)
print(delta)
print(res)
