from requests import *
r = get('https://ojcoms.github.io/genshinoi.github.io/version.info')
with open("information/version.info",'wb') as code:
    code.write(r.content)
