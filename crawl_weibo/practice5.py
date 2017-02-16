
import os

path = 'E:\GIT\practice\Crossin-practices\crawl\weibodata'


allfiles = []
for roots,dir,files in os.walk(path):
    for file in files:
        allfiles.append(roots + os.sep + file)

print(allfiles)