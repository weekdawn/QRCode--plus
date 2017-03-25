#coding=utf-8
import zbar
from PIL import Image
import sys
import threading
import time

reload(sys)
sys.setdefaultencoding('utf-8')

def qr_scan(folder):
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')
	for i in range(100):
		img = Image.open('./'+str(folder)+'/'+str(folder)+str(i)+'.png').convert('L')
		w, h = img.size
		zimg = zbar.Image(w, h, 'Y800', img.tobytes())
		scanner.scan(zimg)
		for s in zimg:
			if not s.data:
				print  "ERROR : "+str(folder)+str(i)+".png is not QRcode!\n"
			else:
				print str(folder)+str(i)+'.png : '+s.data.decode('utf-8').encode('gbk')+"\n"

if __name__ == '__main__':
	
	threads = []
	img_folder = ["is_qrimg","not_qrimg","half_qrimg"]
	thread_num = range(len(img_folder))

	for f in img_folder:
		t = threading.Thread(target=qr_scan, args=(f,))
		threads.append(t)
	
	for i in thread_num:
		threads[i].start()
	
	for i in thread_num:
		threads[i].join()
		