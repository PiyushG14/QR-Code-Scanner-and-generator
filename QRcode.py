import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

link = "https://hackershrine.com"
qr = pyqrcode.create(link)
qr.png("qrcode.png", scale = 6)

qrcode = Image.open("qrcode.png")
display(qrcode)

data = decode(Image.open("qrcode.png"))
print(data[0][0].decode('utf-8'))
