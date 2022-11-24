import qrcode


data = 'QR Code using make() function'

img = qrcode.make(data)

img.save('MYQRCode.png')
