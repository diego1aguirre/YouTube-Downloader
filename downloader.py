from pytube import YouTube
import os

def download_video():
    try:
        url = input("Enter the YouTube URL: ")
        if "youtube.com" not in url:
            print("Please enter a valid YouTube URL.")
            return
        
        yt = YouTube(url)
        print("Title:", yt.title)
        print("Views:", yt.views)

        # Allow user to specify the download directory
        download_folder = input("Enter download folder path (leave empty for current directory): ")
        download_folder = download_folder.strip() or "."

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)
        
        yd = yt.streams.get_highest_resolution()
        
        # Provide feedback during download
        print("Downloading...")
        yd.download(output_path=download_folder)
        
        print("Download complete. Video downloaded to:", download_folder)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    download_video()
