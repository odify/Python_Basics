from datetime import datetime

PYCON_DATE = datetime(year=2020, month=8, day=28, hour=22)

countdown = PYCON_DATE - datetime.now()

print(f"7 Jahre mit Malina zusammen in: {countdown}")