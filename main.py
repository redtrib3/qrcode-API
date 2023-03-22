from fastapi import FastAPI
from io import BytesIO
import qrcode
from starlette.responses import Response


app = FastAPI(
        title="⚡ Qrcode Generator",
        description="`Generate qrcode for any text with custom colors`",
        version='0.0.1',
        redoc_url=None
        )


@app.get('/')
def index():
    return {'detail':"check /docs for API docs.","dev":"github.com/redtrib3"}
    
@app.get('/qrcode')
async def render_qrcode(site: str = None, fg: str = None, bg: str = None, download: str = None):

    if not site:
        return {"ERROR":" 'site' parameter is required","info":"check /docs for documentation" }

    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(site[0:200])
    qr.make(fit=True)

    if fg and bg:
        try:
            img = qr.make_image(fill_color=str(fg), back_color=str(bg))
        except:
            return { 'ERROR': 'Invalid color specified in param fg'}
    else:
        img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)   	# move buffer address pointer to start

    response = Response(content=buffer.getvalue(), media_type="image/png")

    if download:
        # send content disposition header so that the browser force download the image.
        response.headers["Content-Disposition"] = "attachment; filename=qrcode.png"
        return response
    else:
        return response
