#coding=utf-8
import zbar
import sys
import threading
import time

reload(sys)
sys.setdefaultencoding('utf-8')

class MyThread(threading.Thread):
	def __init__(self, func, args, name=''):
		threading.Thread.__init__(self)
		self.name = name
		self.func = func
		self.args = args
		
	def run(self):
		apply(self.func, self.args)
		

def qr_scan(folder):
	scanner = zbar.ImageScanner()
	scanner.parse_config('enable')
	for i in range(100):
		img = Image.open('./'+str(folder)+'/'+str(folder)+str(i)+'.png').convert('L')
		w, h = img.siza
		zimg = zbar.Image(w, h, 'Y800', img.tobytes())
		scanner.scan(zimg)
		for s in zimg:
			if not s.data:
				print "error:This is not QRcode!Please select another photo.\n"
			else:
				print s.data.decode('utf-8').encode('gbk')
	
if __name__ == '__main__':
	
	threads = []
	img_folder = ['is_qrimg','not_qrimg','half_qrimg']
	thread_num = range(len(img_folder))

	for f in img_folder:
		t = MyThread(qr_scan,str(f),qr_scan.__name__)
		threads.append(t)
	
	for i in thread_num:
		threads[i].start()
	
	for i in thread_num:
		threads[i].join()
		
	print 'QRscan Done at '+time.ctime()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	