[![Deploy](https://button.deta.dev/1/svg)](https://deta.sh/)
# Qrcode API for qrcode generation

### Description

API created on _FastAPI_ to generate PNG/JPEG qrcode images. <br><br>
*docs* - https://qrcode-1-j5807843.deta.app/docs


## Endpoints:

<h3> /qrcode </h3><br><br>
<h5> parameters: </h5><br>
```
 'site' -> required : used to specify the string/url to create the qrcode on. 
 'fg'   -> optional : used to specify foreground color of qrcode image.(default: black)
 'bg'   -> optional : used to specify background color of qrcode image.(default: white)

```
 
