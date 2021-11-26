from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)

print("Title: ", yt.title)
print("Length: ", yt.length)
# print(yt.streams.filter(only_video=True, progressive=True))

ys = yt.streams.get_by_itag("394")

ys.download()