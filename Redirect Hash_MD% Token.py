# ?url=https://facebook.com&h=a023cfbf5f1c39bdf8407f28b60cd134
# url = htpps://facebook.com
# token ( hash : md5 ) : a023cfbf5f1c39bdf8407f28b60cd134


import sys, os
import requests

r = requests.get("http://challenge01.root-me.org/web-serveur/ch52/?url=https://google.com&h=99999ebcfdb78df077ad2727fd00969f")
print (r.text)

PHPSESSID:"mj7eudde59kcmaqottlba32de1"
uid:"wKgbZF0aubBmk24FCX3mAg=="