from datetime import datetime
import os
now = datetime.now() # current date and time
statscmd = now.strftime("/bin/sar > /home/VZADCLOUD/v545583/stats/stat.%Y%m%d_%H%M%S")
os.system(statscmd)
