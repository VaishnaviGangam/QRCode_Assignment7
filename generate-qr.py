import qrcode
import os
import sys


# Loading all values from environment
QR_DATA_URL = os.getenv("QR_DATA_URL")
QR_CODE_DIR = os.getenv("QR_CODE_DIR")
QR_CODE_FILENAME = os.getenv("QR_CODE_FILENAME")
FILL_COLOR = os.getenv("FILL_COLOR")
BACK_COLOR = os.getenv("BACK_COLOR")

# Accept URL if sent from args line --url
if len(sys.argv[1:]) > 0 and sys.argv[1] == '--url' and sys.argv[2] is not None:
    QR_DATA_URL = sys.argv[2]

# Assigning defaults if arguments are not provided
if QR_DATA_URL is None:
    QR_DATA_URL = "https://github.com/VaishnaviGangam"
    
if QR_CODE_FILENAME is None:
    QR_CODE_FILENAME = f"qr_001.png"

if FILL_COLOR is None:
    FILL_COLOR = "black"
    
if BACK_COLOR is None:
    BACK_COLOR = "white"


# Generating QR Code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(QR_DATA_URL)
qr.make(fit=True)
img = qr.make_image(fill=FILL_COLOR, back_color=BACK_COLOR)
if QR_CODE_DIR is not None:
    if not os.path.exists(QR_CODE_DIR):
        os.makedirs(QR_CODE_DIR)
    img.save(f'{QR_CODE_DIR}/{QR_CODE_FILENAME}')
    print(f"Generated QR Code for {QR_DATA_URL} at {QR_CODE_DIR}/{QR_CODE_FILENAME}")
else:
    img.save(f'{QR_CODE_FILENAME}')
    print(f"Generated QR Code for {QR_DATA_URL} at {QR_CODE_FILENAME}")
