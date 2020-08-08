import psutil

battery = psutil.sensors_battery()
percent = battery.percent
from pynotifier import Notification

Notification(title='Battery Percentage', description=str(percent) + '% Battery Remaining', duration=5).send()
