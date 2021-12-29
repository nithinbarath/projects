import qrcode


img = qrcode.make("https://youtu.be/vA_GGf-x6hc")
img.save("hey.jpg")