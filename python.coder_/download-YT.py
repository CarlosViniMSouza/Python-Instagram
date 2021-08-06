# pip install pytube

import pytube

link = input("URL Video: ")

video = pytube.YouTube(link)

print(f'Downloading Video: {yt.title}')

stream = video.streams.first()

stream.download(output_patch='./Downloads')

print("Download Completed")