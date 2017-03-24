import zbar
from PIL import Image
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

scanner = zbar.ImageScanner()
scanner.parse_config('enable')
img = Image.open('./halfqr/half_qrimg55.png').convert('L')
w, h = img.size
zimg = zbar.Image(w, h, 'Y800', img.tobytes())

scanner.scan(zimg)

for s in zimg:
	if not s.data:
		print "error:This is not QRcode!\nPlease select another photo."
	else:
		print s.data.decode('utf-8').encode('gbk')