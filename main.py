from pytube import YouTube
import os
from moviepy.editor import VideoFileClip, AudioFileClip


downloads_folder = 'downloads'
audio_downloads_folder = 'downloads/audio'

if not os.path.exists(downloads_folder):
    os.makedirs(downloads_folder)

if not os.path.exists(audio_downloads_folder):
    os.makedirs(audio_downloads_folder)

def get_links():
    links = []
    with open('links.txt', 'r') as file:
        for line in file:
            links.append(line.strip())
    return links

def download_video(link):
    yt = YouTube(link)
    print(f'Downloading {yt.title}...')
    yt.streams.get_highest_resolution().download(output_path=downloads_folder)
    print(f'{yt.title} downloaded successfully!')

def convert_mp4_to_mp3():
    for file in os.listdir(downloads_folder):
        if file.endswith('.mp4'):
            video = VideoFileClip(f'{downloads_folder}/{file}')
            audio = video.audio
            audio.write_audiofile(f'{audio_downloads_folder}/{file[:-4]}.mp3')
            audio.close()
            video.close()
            print(f'{file} converted to mp3 successfully!')

def download_all(links):
    for link in links:
        try:
            download_video(link)
        except:
            print(f'Failed to download {link}!')
            with open('failed_links.txt', 'a') as file:
                file.write(f'{link}\n')
            continue
def main():
    links = get_links()
    if input('Do you want to download both video and audio files? (y/n) ').lower() == 'y':
        download_all(links)
        convert_mp4_to_mp3()
    else:
        download_all(links)
        
if __name__ == '__main__':
    main()