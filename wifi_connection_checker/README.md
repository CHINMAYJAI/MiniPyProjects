# Wi-Fi Status Notification Script

This Python script monitors the Wi-Fi connection status and shows a notification when the Wi-Fi is disconnected. The notification will be shown only once after the Wi-Fi is disconnected and will not be repeated until it reconnects and disconnects again.

## Features

- Monitors Wi-Fi connection status in real-time.
- Sends a notification if Wi-Fi is disconnected.
- Notifications are shown only once after disconnection and are not repeated until reconnected.

## Requirements

To run this script, you need:

- Python 3.x
- `winotify` (for showing notifications)
- `socket` (for checking Wi-Fi connection)

### Install the dependencies:

You can install the required libraries using:

```bash
pip install winotify
```

### How to Use
1. Running the Script in Python
If you want to run the script as a Python file:

1.Clone or download the repository.\
2.Run the script using Python:
```bash
python script.py
```
The script will continuously monitor your Wi-Fi connection and show notifications if the Wi-Fi is disconnected.

2. Convert to Executable Format
To make the script run as an executable file (so you don't need to manually run it through Python every time), follow these steps:

**Step 1: Install PyInstaller**\
Install PyInstaller to convert the Python script into a .exe (Windows) or executable (Linux/macOS).
```bash
pip install pyinstaller
```
**Step 2: Generate Executable File**\
-- Windows: In the directory containing your script, run the following command in the terminal:
```bash
pyinstaller --onefile script.py
```
This will generate an executable in the dist folder.

-- Linux/macOS: Use the same command to generate the executable for Linux or macOS:
```bash
pyinstaller --onefile script.py
```
The executable will also be located in the dist folder.

**Step 3: Set Permissions for Executable (Linux/macOS)**\
For Linux or macOS, you may need to give the executable permission to run:
```bash
chmod +x dist/script
```
**Step 4: Run the Executable**\
Windows: Double-click the .exe file in the dist folder to run it.
Linux/macOS: Run the executable from the terminal:

```bash
./dist/script
```
### 3. Automatically Start the Script on Boot
#### Windows
1. Press Win + R, type shell:startup, and press Enter.
2. Place the .exe file from the dist folder into the Startup folder to run the script automatically when Windows starts.
#### Linux
1. Using Cron: You can set the script to run automatically at startup using Cron. Edit the cron jobs with:

```bash
crontab -e
```
Add this line to the crontab file:
```bash
@reboot /path/to/your/executable
```
2. Using .desktop File: Create a .desktop file in the ~/.config/autostart/ directory to automatically launch the script at startup.

## Contribution

Feel free to fork the repository and submit a pull request if you'd like to improve this project. Suggestions and feedback are welcome!

## Author

[Chinmay Jain](https://github.com/CHINMAYJAI)









