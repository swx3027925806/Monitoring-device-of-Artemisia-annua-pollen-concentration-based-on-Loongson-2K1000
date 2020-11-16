import os
count = 0
path = '/home/loongson/darknet/photo'
files = os.listdir(path)
for i, file in enumerate(files):
    count += 1
    NewName = os.path.join(path, "%03d.bmp"%count)
    OldName = os.path.join(path, file)
    os.rename(OldName, NewName)
