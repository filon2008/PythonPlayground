import urllib
def savehzplanning(url):
    urls = url.split('image=')
    asciis = urls[1].split('%u')[1:]
    pmsg = ''.join([chr(int(x, 16)) for x in asciis])
    image_url = '/'.join(urls[0].split('/')[:3]) + pmsg
    urllib.request.urlretrieve(image_url, pmsg.split('/')[-1])
