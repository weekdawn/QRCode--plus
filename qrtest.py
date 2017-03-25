#coding=utf-8
import qrcode
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

qr = qrcode.QRCode(
	version = 2,	#表示生成二维码的尺寸大小[1,40]
	error_correction = qrcode.constants.ERROR_CORRECT_L,#制定二维码的容错系统L,M,Q,H
	box_size = 5,	#表示每个格子的像素大小
	border = 1	#表示边框的格子厚度是多少（默认为4）

	)

qr.add_data("http://www.baidu.com")
qr.make(fit=True)
img = qr.make_image()
img.save("test001.png")