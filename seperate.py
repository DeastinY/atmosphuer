import os, codecs, youtube_dl
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

class Song():
    def __init__(self, link="", name="", category=""):
        self.link=link
        self.name=name
        self.category=category

    def __str__(self):
        return "{0} : {1} - {2}".format(self.name,self.category, self.link)

    def __repr__(self):
        return self.__str__()

def haslink(c):
    return "http" in c

def getlink(c):
    split = c.split(" ")
    for s in split:
        if haslink(s):
            return s.strip()

def getname(c):
    if ':' in c:
        return c.split(':')[0].strip()
    else:
        return c.strip()

def load(s):
    ydl_opts={
        'format': 'bestaudio/best',
        'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        #'quiet': True,
        'restrictfilenames' : True
    }
    print("Loading "+str(s))
    ydl_opts['outtmpl'] = s.category+' - '+s.name+'.%(ext)s'
    print (ydl_opts)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([s.link])
        except:
            pass

with codecs.open(os.path.join(os.getcwd(), "m.txt"),'r',encoding='utf-8', errors='ignore')  as f:
  content = f.readlines()

songs=[]
category = "no category"
for c in content:
    c = c.strip()
    if haslink(c):
        c = c.replace(",","")
        songs.append(Song(link=getlink(c),category=category, name=getname(c)))
    else:
        if len(c) > 1: # ignore linkebreaks
            if ':' in c:
                category = c.split(":")[0].strip()
            else:
                category = c.strip()

pool = ThreadPool(4)

results = pool.map(load,songs)

pool.close()
pool.join()
