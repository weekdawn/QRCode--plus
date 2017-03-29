#coding=utf-8
import zbar
from PIL import Image
import sys
import os
import re

reload(sys)
#设置系统默认编码方式，避免中文乱码
sys.setdefaultencoding('utf-8')
#创建zbar扫描器

def qrScan(file_name):
	global key
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
			data_file.write( str(key) + "=" + s.data.decode('utf-8').encode('gbk') + "\n")
			
if __name__ == '__main__':
	#配置ini文件
	section = "[Qrdata]"
	key = "value1"
	#判断ini文件是否有section,和重复的value
	match_section = re.compile(section)
	match_key = re.compile(key)
	#判断是否存在output文件夹，若不存在则创建
	if not os.path.exists("output"):
		os.mkdir("output")
	data_file = open("./output/qr_data.ini", "a+")
	#定位到文件首位
	data_file.seek(0,0)
	first_line = data_file.readline()
	#如果文首没有匹配到section自动添加进去
	if not re.search(match_section, first_line):
		data_file.seek(0,0)
		data_file.write(str(section)+"\n")
	#定位到文首
	data_file.seek(0,0)
	all_ini = data_file.read()
	#匹配是否有重复的key
	while re.search(match_key, all_ini):
		new_key = str( int(key[5:]) + 1 )
		key = key[:5] + new_key
		match_key = re.compile(key)
	#定位到文末
	data_file.seek(0,2)
	#从命令行接收文件路径
	file_name = sys.argv[1]
	q = qrScan(file_name)
	print "Scan QrCode successed!"
	data_file.close()