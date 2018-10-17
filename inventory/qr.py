from PIL import Image
import qrcode

input = '1'

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=2,
    border=4
)

qr.add_data(input)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

img.save('test.png')