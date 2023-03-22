[![Deploy](https://button.deta.dev/1/svg)](https://deta.sh/)
# Qrcode API for qrcode generation

### Description

API created on _FastAPI_ to generate PNG/JPEG qrcode images. <br><br>
*docs* - https://qrcode-1-j5807843.deta.app/docs


## Endpoints:

## _/qrcode_
<h5> parameters: </h5>

```
 'site' -> required : used to specify the string/url data to create the qrcode on. 
 'fg'   -> optional : used to specify foreground color of qrcode image.(default: black)
 'bg'   -> optional : used to specify background color of qrcode image.(default: white)
 'download' -> optional : specify this param with any value to download the image. 

```
## Example:

Create a Qr-code with data "http://github.com" :

` URL: https://qrcode-1-j5807843.deta.app/qrcode?site=http://github.com `

![qrcode-def](https://qrcode-1-j5807843.deta.app/qrcode?site=http://github.com)

Create a Qr-code with data "hello" and Foreground color Black and Background color Cyan:

` URL: https://qrcode-1-j5807843.deta.app/qrcode?site=hello&fg=black&bg=cyan `

![qrcode](https://qrcode-1-j5807843.deta.app/qrcode?site=hello&fg=black&bg=cyan)

To download the image add the parameter 'download'.

` URL:  https://qrcode-1-j5807843.deta.app/qrcode?site=hello&fg=black&bg=cyan&download=y `
 
