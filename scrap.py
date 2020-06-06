from pytube import YouTube
import sys
url =input("Enter the Youtube link to Download : ")
yt=YouTube(url)
print("\n\nTitle of the video : " +str(yt.title))

r=input("\n\nEnter the Quality (360p,720p) : ")
res=['360p','720p']
if r not in res:
    print("\nQuality not found.Searching for 360p (Default)")
    r='360p'
index=res.index(r)  
videos =yt.streams.order_by("resolution").desc().filter(progressive=True)
# for v in videos:
#     print(v)
flag=True
i=0
if len(videos)==0:
    flag=False
    videos =yt.streams.order_by("resolution").desc().filter(progressive=True,res=res[0])

if len(videos)==0:
    print("File not found !")
    sys.exit()

if flag ==False:
    print("\n\nFile not found in specified Quality. Trying... on another one!")
    print("\nDownloading video on "+str(res[0]))
    print("")

print("\nDownloading....")
videos.first().download()
print("\nCompleted...")
a=input()
sys.exit()

