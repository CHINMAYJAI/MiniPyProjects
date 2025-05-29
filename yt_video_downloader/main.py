# Importing necessary modules
from moviepy.editor import VideoFileClip, AudioFileClip  # For video and audio processing
import subprocess  # For running external commands
from tqdm import tqdm  # For displaying progress bars
import os  # For interacting with the operating system
import shutil  # For file operations like removing directories

def print_separator(message):
    """Function to print formatted separators with a message."""
    print("\n" + "=" * 60)  # Print a line of equal signs
    print(f"{message.center(60)}")  # Center the message
    print("=" * 60 + "\n")  # Print another line of equal signs

def audioDownloader(url):
    """Function to download audio from a given URL using yt-dlp."""
    print_separator("Downloading Audio")
    
    # Ensure the media/audio folder exists; create it if it doesn't
    if not os.path.exists("media/audio"):
        os.makedirs("media/audio")

    # Construct the yt-dlp command for downloading audio
    powershell_command = f'yt-dlp -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 -o "media/audio/%(title)s.%(ext)s" "{url}"'

    # Run yt-dlp command in a subprocess and capture output incrementally
    with subprocess.Popen(["powershell", "-Command", powershell_command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as process:
        # Simulate progress using tqdm
        with tqdm(desc="Downloading Audio", unit="item") as pbar:
            for line in process.stdout:
                print(f"[INFO] {line.strip()}")  # Print the output from yt-dlp
                pbar.update(1)  # Increment the progress bar

    print_separator("Audio Downloaded Successfully and Saved in 'media/audio'")

def videoWithoutAudioDownloader(url):
    """Function to download video without audio from a given URL using yt-dlp."""
    print_separator("Downloading Video")

    # Ensure the media/video folder exists; create it if it doesn't
    if not os.path.exists("media/video"):
        os.makedirs("media/video")

    # Construct the yt-dlp command for downloading video
    powershell_command = f'yt-dlp -f bestvideo -o "media/video/%(title)s.%(ext)s" "{url}"'

    # Run yt-dlp command in a subprocess and capture output in real-time
    with subprocess.Popen(["powershell", "-Command", powershell_command], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True) as process:
        with tqdm(desc="Downloading Video", unit="chunk", bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} {unit}") as pbar:
            for line in process.stdout:
                print(f"[INFO] {line.strip()}")  # Print the output from yt-dlp
                pbar.update(1)  # Increment the progress bar

    print_separator("Video Downloaded Successfully and Saved in 'media/video'")

def fetchFileNames():
    """Fetch file names of the latest video and audio files from their respective directories."""
    video_dir = "media/video"  # Directory for downloaded videos
    audio_dir = "media/audio"  # Directory for downloaded audio

    # Get the latest video file with specific extensions
    video_files = [f for f in os.listdir(video_dir) if f.endswith((".mp4", ".mkv", ".webm"))]
    # Get the latest audio file with specific extensions
    audio_files = [f for f in os.listdir(audio_dir) if f.endswith((".mp3", ".opus", ".webm"))]

    # Check if both video and audio files exist
    if video_files and audio_files:
        return os.path.join(video_dir, video_files[0]), os.path.join(audio_dir, audio_files[0])
    else:
        print_separator("Error: No Matching Video or Audio Files Found")
        return None, None

def videoAudioMerger():
    """Function to merge downloaded audio and video files into a single video file."""
    print_separator("Merging Audio & Video")

    video_path, audio_path = fetchFileNames()  # Fetch the latest video and audio file paths

    # Check if both paths are valid
    if video_path and audio_path:
        video = VideoFileClip(video_path)  # Load the video file
        audio = AudioFileClip(audio_path)  # Load the audio file

        video = video.set_audio(audio)  # Set the audio to the video
        output_path = "media/video.mp4"  # Define output path for merged video
        video.write_videofile(output_path, codec="libx264", audio_codec="aac")  # Write the merged video file

        print_separator(f"Merge Successful! Saved as {output_path}")
    else:
        print_separator("Error: Cannot Merge Files Because One or Both Are Missing")

def removeFolder():
    """Function used to remove the unnecessary files and folders after processing."""
    # Check if both media folders exist
    if os.path.exists("media/video") and os.path.exists("media/audio"):
        shutil.rmtree("media/video")  # Remove video folder
        shutil.rmtree("media/audio")   # Remove audio folder
        print("Unnecessary files are removed")
    else:
        print("No such files and directory exists!")

# Ensure the main media folder exists; create it if it doesn't
if not os.path.exists("media"):
    os.makedirs("media")

# Get URL from user input
url = input("\n" + "=" * 60 + "\nEnter video URL: ".center(60) + "\n" + "=" * 60 + "\n")

# Execute download functions in sequence
audioDownloader(url)  # Download audio
videoWithoutAudioDownloader(url)  # Download video without audio
videoAudioMerger()  # Merge audio and video into one file
removeFolder()  # Clean up unnecessary files and folders