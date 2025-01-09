# importing necessary modules
from winotify import Notification, audio
import psutil
import time

# infinite loop to constantly check battery status
while True:
    # get battery details
    battery = psutil.sensors_battery()
    percent = battery.percent
    power_plugged = battery.power_plugged
    
    # check if the battery is fully charged and the power is plugged in
    if power_plugged == True and percent == 100:
        # create and show notification
        notification = Notification(
            app_id="Charging Status",
            title="Fully Charged!",
            msg="Battery is fully charged, please unplug your charger!",
            icon=r"E:\codes\development\software_development\full_charging_notification\fully_charged_image.ico",
            duration="short",
        )
        notification.set_audio(audio.Default, loop=False)
        notification.show()
    
    # wait for 60 seconds before checking again
    time.sleep(60)