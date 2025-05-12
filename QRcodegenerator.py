import qrcode

data = input('Enter the text or URL: ').strip()
filename = input('Enter the file name: ').strip()

qrcode = qrcode.QRCode(box_size=10, border=4)
qrcode.add_data(data)

image = qrcode.make_image(fill_color='black', back_color='white')
image.save(filename)
print(f'QR code saved as {filename}')
