# YouTube Video and Audio Downloader

This Python project leverages the 'pytube' and 'moviepy' libraries to download YouTube videos, optionally converting them to MP3 audio files.

## Prerequisites

-   **Python 3** ([https://www.python.org/downloads/](https://www.python.org/downloads/))
-   **Required packages:**
    -   `pytube`
    -   `moviepy`

## Setup

1. **Install dependencies**

```bash
pip install -r requirements.txt
```

2. **(Optional) Modify download folders:**
   If you wish to change the default download folders ('downloads' and 'downloads/audio'), modify the `downloads_folder` and `audio_downloads_folder` variables in the script.

## Usage

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Choose download options:**
   The script will ask if you want to download both video and audio.
    - Type 'y' to download both and convert videos to MP3.
    - Type 'n' to download videos only.

## Explanation

The script performs the following:

-   **Import Libraries:** Imports the `pytube`, `os`, `VideoFileClip`, and `AudioFileClip` libraries.
-   **Folder Setup:** Creates 'downloads' and 'downloads/audio' folders if they don't exist.
-   **`get_links()`** Reads YouTube video links from 'links.txt'.
-   **`download_video()`** Downloads videos using pytube and prints progress.
-   **`convert_mp4_to_mp3()`** Converts downloaded MP4 files to MP3 (if the user chose to do so).
-   **`download_all()`** Iterates through the links, calling `download_video()`.
-   **`main()`** Handles user input and coordinates the download and conversion process.
