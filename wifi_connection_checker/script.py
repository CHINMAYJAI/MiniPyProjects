import socket
from winotify import Notification, audio
import time

# Define a function to check Wi-Fi connection
def is_wifi_connected():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

# Initialize the connection status
was_connected = True  # Assume the Wi-Fi starts as connected

# Start an infinite loop to monitor Wi-Fi connection
while True:
    # Check the current Wi-Fi connection status
    current_connection = is_wifi_connected()

    # If Wi-Fi is disconnected and was previously connected, show a notification
    if not current_connection and was_connected:  # Wi-Fi disconnected and previously was connected
        notification = Notification(
            app_id="Wifi Status",
            title="WiFi is not connected",
            msg="WiFi is not connected, please connect it to the network",
            duration="short",
        )
        notification.set_audio(audio.Default, loop=False)
        notification.show()

    # Update the previous connection status
    was_connected = current_connection  # Update the previous connection status

    # Wait for 10 seconds before checking again
    time.sleep(10)