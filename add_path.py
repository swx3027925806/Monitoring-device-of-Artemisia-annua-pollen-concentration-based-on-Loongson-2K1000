import os
image_path = '/home/loongson/darknet/photo'
f = open('myData_test.txt', 'r+')
f.truncate()
dirs = os.listdir(image_path)
for item_file in dirs:
	f.write(image_path + '/' + item_file + '\n')
f.close()
