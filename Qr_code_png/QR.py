<<<<<<< HEAD
import qrcode
from PIL import Image

import RANDOMNUMBER as usc
import colors

# The file path/link of the logo pasted in the QR code
Logo_link = 'C:/Users/marco/Pictures/Website/stadsknaal74.png'
logo = Image.open(Logo_link)
basewidth = 64
wpercent = (basewidth / float(logo.size[1]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
# Ask input link for the qr code
url = str(input('Link to make a qr code with: '))
QRcode.add_data(url)
QRcode.make()
# choose a color from the color list function
QRcolor = input(f'{colors.colorlist()}\n'
                f'Choose a color for the qr code itself:')
backgroundcolour = QRcode.make_image(fill_color=QRcolor, back_color=input(f'{colors.colorlist()}\n'
                                                                          f'Choose a color for the background of the '
                                                                          f'qr code:')).convert(
    'RGB')
pos = ((backgroundcolour.size[1] - logo.size[1]) // 2, (backgroundcolour.size[1] - logo.size[1]) // 2)
backgroundcolour.paste(logo, pos)
Filename = usc.usesleft()
Filename = str(Filename)
backgroundcolour.save(f'C:/Users/marco/Desktop/{Filename}.png')
print('QR code generated!')
=======
import qrcode
from PIL import Image

import RANDOMNUMBER as usc
import colors

# The file path/link of the logo pasted in the QR code
Logo_link = 'C:/Users/marco/Pictures/Website/stadsknaal74.png'
logo = Image.open(Logo_link)
basewidth = 64
wpercent = (basewidth / float(logo.size[1]))
hsize = int((float(logo.size[1]) * float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
# Ask input link for the qr code
url = str(input('Link to make a qr code with: '))
QRcode.add_data(url)
QRcode.make()
# choose a color from the color list function
QRcolor = input(f'{colors.colorlist()}\n'
                f'Choose a color for the qr code itself:')
backgroundcolour = QRcode.make_image(fill_color=QRcolor, back_color=input(f'{colors.colorlist()}\n'
                                                                          f'Choose a color for the background of the '
                                                                          f'qr code:')).convert(
    'RGB')
pos = ((backgroundcolour.size[1] - logo.size[1]) // 2, (backgroundcolour.size[1] - logo.size[1]) // 2)
backgroundcolour.paste(logo, pos)
Filename = usc.usesleft()
Filename = str(Filename)
backgroundcolour.save(f'C:/Users/marco/Desktop/{Filename}.png')
print('QR code generated!')
>>>>>>> ec58f8cda52865816fd5d8177f34b0bd8f33384e
