import pyqrcode as qr
import qrcode

img =qrcode.make("https://gyanlabap.com/")
img.save('gyanlab.png')
