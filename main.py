from pytube import YouTube
import sys
url =input("Enter the Youtube link to Download : ")
yt=YouTube(url)
print("\n\nTitle of the video : " +str(yt.title))

r=input("\n\nEnter the Quality (144p,240p,360p,480p,720p,1080p) : ")
res=['144p','240p','360p','480p','720p','1080p']
if r not in res:
    print("\nQuality not found.Searching for 480p (Default)")
    r='480p'
index=res.index(r)  
videos =yt.streams.order_by("resolution").desc().filter(file_extension='mp4',fps=30,res=r)
flag=True
i=0
while len(videos)==0:
    flag=False
    videos =yt.streams.order_by("resolution").desc().filter(file_extension='mp4',fps=30,res=res[index-i])
    i=i+1
if flag ==False:
    print("\n\nFile not found in specified Quality. Trying... on another one!")
    print("\nDownloading video on "+str(res[index-i+1]))
    print("")

print("\nDownloading....")
videos.first().download("C:\\Users\\RUDRA\\Desktop\\python\\youtube")
print("\nCompleted...")
a=input()
sys.exit()

