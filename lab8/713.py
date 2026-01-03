from datetime import datetime

dt = datetime.strptime("2025-11-11 11:11:11", "%Y-%m-%d %H:%M:%S")
print(dt.strftime("%Y-%m-%d %H:%M:%S"))