from datetime import datetime
date1 = datetime(2023, 2, 18, 15, 35, 0)
date2 = datetime(2023, 2, 18, 12, 30, 0)
diff = date1 - date2

diff = diff.total_seconds()
print(diff)
