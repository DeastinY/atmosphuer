import os, codecs

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
            return s

def getname(c):
    if ':' in c:
        return c.split(':')[0]
    else:
        return c

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
                category = c.split(":")[0]
            else:
                category = c

for s in songs:
    print(s)
