#coding=utf-8
import zbar
from PIL import Image
import sys
import threading
import time
import os

reload(sys)
sys.setdefaultencoding('utf-8')

class MyThread(threading.Thread):
	def __init__(self, func, args):
		threading.Thread.__init__(self)
		self.func = func
		self.args = args
	
	def run(self):
		apply(self.func, self.args)

def qr_scan(folder):
	global n
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')
	for root,dir,file in os.walk(folder):
		for i in file:
			img = Image.open(root+"/"+i).convert('L')
			w, h = img.size
			zimg = zbar.Image(w, h, 'Y800', img.tobytes())
			scanner.scan(zimg)
			n += 1
			for s in zimg:
				if not s.data:
					print  "ERROR : "+str(i)+" is not QRcode!\n"
				else:
					print str(i)+":"+s.data.decode('utf-8').encode('gbk')+"\n"

if __name__ == '__main__':
	
	threads = []
	img_folder = []
	for i in range(1,4):
		tmp = raw_input("Please input three QR-image's path (input enter to default),"+str(i)+":")
		if tmp:
			img_folder.append(tmp)
	if not img_folder:
		img_folder = [r".\half_qrimg",r".\is_qrimg",r".\not_qrimg"]
	
	thread_num = range(len(img_folder))
	
	start = time.time()
	n = 0
	for f in img_folder:
		t = MyThread(qr_scan,(f,))
		threads.append(t)
	
	for i in thread_num:
		threads[i].start()
	
	for i in thread_num:
		threads[i].join()
		
	spend = time.time() - start
	print "总耗时：" + str(spend) + "秒"
	print "共扫描" + str(n) + "张图片"
		
		
		
		
		
		
		