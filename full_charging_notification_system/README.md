# MiniPyProject

A lightweight Python project that provides a desktop notification when your battery is fully charged and plugged in. This utility ensures you unplug your charger at the right time to preserve battery health.

## Features

- Monitors the battery status continuously.
- Sends a desktop notification when the battery is fully charged and the charger is still plugged in.
- Plays a notification sound for user alert.

## Requirements

- Python 3.6 or higher
- `winotify` library
- `psutil` library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/CHINMAYJAI/MiniPyProject.git
   ```
2. Navigate to the project directory:
   ```bash
   cd MiniPyProject
   ```
3. Install the required Python libraries:
   ```bash
   pip install winotify psutil
   ```

## Usage

1. Update the `icon` path in the code to point to the location of your `.ico` file.
2. Run the script:
   ```bash
   python script.py
   ```
3. The script will monitor your battery status and notify you when the battery is fully charged and plugged in.

## Customization

- **Notification Icon**: Replace the `icon` path in the script with your desired `.ico` file.
- **Notification Interval**: Change the `time.sleep(60)` value to modify the check interval (in seconds).

## Creating an Executable

To create a standalone executable for this project using `pyinstaller`, use the following command:
```bash
pyinstaller --onefile --noconsole --add-data "IMAGE_LOCATION;." FILE_LOCATION
```
Replace `IMAGE_LOCATION` with the path to your `.ico` file and `FILE_LOCATION` with the path to your Python script.

Make that script startup executable, so at system starts it will automatically executed

## File Structure

```
MiniPyProject/
├── script.py         # Main script file
├── README.md         # Project documentation
└── fully_charged_image.ico  # Icon for the notification (optional)
```


## Contribution

Feel free to fork the repository and submit a pull request if you'd like to improve this project. Suggestions and feedback are welcome!

## Author

[Chinmay Jain](https://github.com/CHINMAYJAI)