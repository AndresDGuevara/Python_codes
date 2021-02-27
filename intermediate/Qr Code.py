import pyqrcode
import png 

from pyqrcode import QRCode

QRstring = "https://www.youtube.com/watch?v=HvgZsf5jN-0&ab_channel=JonnoBrien-Topic" # Paste any url here

url = pyqrcode.create(QRstring)
url.png('Desktop\\qr.png', scale = 8)