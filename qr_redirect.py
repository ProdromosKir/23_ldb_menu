import qrcode

url = "https://two3-ldb-menu.onrender.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,

)
qr.add_data(url)
qr.make(fit=True)

qr_image = qr.make_image(fill="black",back_color="white")
qr_image.save("menu_qr_code.png")
print("QR Code generated succesfully!")
