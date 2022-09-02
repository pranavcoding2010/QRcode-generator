import pyqrcode
import png
from pyqrcode import QRCode
s = "https://dashboard.campk12.com"
url = pyqrcode.create(s)
url.svg("My url.svg",scale = 8)
url.png("My url.png",scale = 6)