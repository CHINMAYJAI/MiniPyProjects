# YT VIDEO DOWNLOADER

**YT VIDEO DOWNLOADER** is a Python-based tool designed to download videos and audio from YouTube using the `yt-dlp` library. This project allows users to easily download their favorite content in various formats and merge audio and video files seamlessly.

## CAUTION:

- **The tool is for educational purposes only.**

- **It should only be used for content you are legally allowed to download.**

- **You do not support or encourage illegal downloading.**

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Contributing](#contributing)
- [License](#license)

## Features

- Download audio in MP3 format.
- Download video without audio in various formats.
- Merge downloaded audio and video into a single file.
- Clean up unnecessary files after processing.

## Installation

To use the `yt_video_downloader`, you need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Required Libraries

This project requires the following libraries:

- `moviepy`: For video and audio processing.
- `tqdm`: For displaying progress bars.
- `yt-dlp`: For downloading videos from YouTube.

You can install the required libraries using pip:

```bash
pip install moviepy tqdm yt-dlp
```

## Usage

1. **Clone the repository**:
   ```bash
    git clone https://github.com/CHINMAYJAI/MiniPyProjects.git
    cd MiniPyProjects/yt_video_downloader
   ```

2. **Run the script**:
   Execute the script in your terminal or command prompt:
   ```bash
   python main.py
   ```

3. **Enter the video URL**:
   When prompted, enter the URL of the YouTube video you wish to download.

4. **Follow the prompts**:
   The script will download the audio and video, merge them, and notify you when the process is complete.

## Functions

### `audioDownloader(url)`
Downloads audio from the specified YouTube URL and saves it in the `media/audio` directory.

### `videoWithoutAudioDownloader(url)`
Downloads video without audio from the specified YouTube URL and saves it in the `media/video` directory.

### `fetchFileNames()`
Fetches the latest video and audio file names from their respective directories.

### `videoAudioMerger()`
Merges the downloaded audio and video files into a single video file.

### `removeFolder()`
Removes the `media/audio` and `media/video` directories after processing to clean up unnecessary files.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and submit a pull request. Ensure that your contributions include:

- A clear description of the changes made.
- Any relevant documentation updates.
- Tests for new features, if applicable.

## License

This project is licensed under the MIT License. Feel free to use the code in this project for personal or commercial purposes.

---

Thank you for using **yt_video_downloader**! We hope you find it useful for downloading and managing your favorite YouTube content. If you have any questions or feedback, please feel free to reach out.

## Author

**Chinmay Jain**  
[GitHub Profile](https://github.com/CHINMAYJAI)