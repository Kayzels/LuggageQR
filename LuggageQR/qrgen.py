import urllib.parse
import qrcode
from qrcode.image import svg
from LuggageQR.constants import *

WHATSAPP_LINK = "https://wa.me/"
DEFAULT_MESSAGE = "Hi. I have your luggage."
SVG_FACTORY = svg.SvgPathImage

def createCode(cell_no: str, message: str = DEFAULT_MESSAGE) -> qrcode.QRCode:
    """Create a QRCode object that will create a WhatsApp message
    to send to the given number 
    """
    cell_no = cell_no.replace(" ", "")
    if cell_no[0] == "+":
        cell_no = cell_no[1:]
    message = urllib.parse.quote_plus(message)
    code = qrcode.QRCode(version=1, box_size=10, border=5)
    link = WHATSAPP_LINK + cell_no + "?text=" + message
    code.add_data(link)
    code.make(fit=True)
    return code

def createSVGCode(code: qrcode.QRCode) -> bytes:
    img = code.make_image(image_factory=SVG_FACTORY)
    svg_xml: bytes = img.to_string() # type: ignore
    return svg_xml

def generateQR_XML(cell_no: str, message: str = DEFAULT_MESSAGE) -> bytes:
    """Create an SVG in XML bytes format which contains the data
    for a WhatsApp message

    Returns:
        bytes: SVG Data in byte form
    """
    code = createCode(cell_no, message)
    return createSVGCode(code)
