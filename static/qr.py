import qrcode

url = "https://hotel-menu-qr.onrender.com/menu?table=5"

img = qrcode.make(url)
img.save("table5_qr.png")

print("✅ QR Code saved as table5_qr.png")
