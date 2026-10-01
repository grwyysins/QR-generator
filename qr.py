import qrcode
#Text or URL to encode
data = ""
#Create a QR code
qr= qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)
#Save the image
img = qr.make_image(fill_color="black",back_color="white")
img.save(r"C:\Users\Administrator\Desktop\Python\Mine\QRs\.png")