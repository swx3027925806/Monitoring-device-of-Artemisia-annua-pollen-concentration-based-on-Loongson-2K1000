#-*-coding:utf-8-*-
import re

count = 0
count2 = 0

f = open("./test.c", 'r')
temp = f.read()
answer = re.findall('huanghuahao:(.*?)%',temp)

for item in answer:
	if eval(item) == 100:
		count += 1
	elif eval(item) > 98:
		count2 += 1

print "黄花蒿确定个数:"+str(count)
print "黄花蒿疑似个数:"+str(count2)
f.close()
