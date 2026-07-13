# pip install qrcode
# pip install Pillow

import sys
import qrcode

if len(sys.argv) > 1:
    value = sys.argv[1]
else:
    value = input("Enter your text: ")

qr = qrcode.make(value)
qr.save(f"{value}.png")

# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_M,
#     box_size=10,
#     border=4
# )
# qr.add_data(input("Enter your text: "))
# qr.make(fit=True)
# img = qr.make_image(fill_color="green", back_color="white")
# img.save("qr.png")
