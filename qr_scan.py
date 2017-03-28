#coding=utf-8
import zbar
from PIL import Image
import sys

reload(sys)
#设置系统默认编码方式，避免中文乱码
sys.setdefaultencoding('utf-8')
#创建zbar扫描器

def qrScan(file_name):
	scanner = zbar.ImageScanner()
	#打开zbar解析配置
	scanner.parse_config('enable')
	#打开需要扫描的二维码
	img = Image.open(file_name).convert('L')
	#获取二维码图片的宽和高
	w, h = img.size
	#将图片数据传入扫描器
	zimg = zbar.Image(w, h, 'Y800', img.tobytes())
	scanner.scan(zimg)
	for s in zimg:
		if not s.data:
			print "error:This is not QRcode!\nPlease select another photo."
		else:
			data_file.write( "value : " + s.data.decode('utf-8').encode('gbk') + "\n")
			

if __name__ == '__main__':
	data_file = open("qr_data.ini", "a")
	data_file.write("[Config]\n")
	name = raw_input("Please input QRcode's name:")
	q = qrScan(name)