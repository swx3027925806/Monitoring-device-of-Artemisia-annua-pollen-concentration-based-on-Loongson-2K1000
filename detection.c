#include<stdio.h>
int main(){
	system("python rename.py");
	system("python add_path.py");
	system("./darknet detector test cfg/voc.data cfg/yolov3-tiny.cfg yolov3-tiny_last.weights < path.c > test.c");
	system("python tofind.py > anwser.c");
	return 0;
}
