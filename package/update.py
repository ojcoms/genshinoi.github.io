from requests import *
r = get('https://ojcoms.github.io/genshinoi.github.io/version.info')
with open("information/version.info",'wb') as code:
    code.write(r.content)

with open("information/version.info",'r') as code:
    new = code.read()
with open("information/nowversion.info",'r') as code:
    now = code.read()
if now != new:
    r = get('https://ojcoms.github.io/genshinoi.github.io/package/main.py')
    with open("main.py",'wb') as code:
        code.write(r.content)
    with open("information/nowversion.info",'w+') as code:
        code.write(new)
