from pathlib import Path
import qrcode
from LuggageQR.constants import *

WHATSAPP_LINK = "https://wa.me/"
DEFAULT_MESSAGE = "Hi. I have your luggage."

def createCode(cell_no: str, message: str = DEFAULT_MESSAGE) -> qrcode.QRCode:
    """Create a QRCode object that will create a WhatsApp message
    to send to the given number 
    """
    code = qrcode.QRCode(version=1, box_size=10, border=5)
    link = WHATSAPP_LINK + cell_no + "?text=" + message
    code.add_data(link)
    code.make(fit=True)
    return code

def createQRImage(code: qrcode.QRCode, file_name: Path = QR_FILE_NAME_BASE) -> None:
    """Generate a PNG image of the QR Code in the location 
    specified by file_name
    """
    png_name = str(file_name.resolve().with_suffix('.png'))
    img = code.make_image(fill='black', back_color='white')
    img.save(png_name)

def generateQR(cell_no: str, message: str = DEFAULT_MESSAGE, file_name: Path = QR_FILE_NAME_BASE):
    """Create a png image of a Whatsapp QR Code that will send a given message
    """
    code = createCode(cell_no, message)
    createQRImage(code, file_name)
