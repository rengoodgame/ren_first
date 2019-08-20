
from urllib import request
import chardet

if __name__ == '__main__':
    url = "https://www.douyu.com/directory/all"

    rsp = request.urlopen(url)

    html= rsp.read()


    cs = chardet.detect(html)

    print(cs)

 
