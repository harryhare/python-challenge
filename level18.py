import urllib2
import urllib
import cookielib
import re
cookie_say="BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90"
if(cookie_say==""):
    level_url='http://www.pythonchallenge.com/pc/return/romance.html'
    nothing_url="http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
    begin=12345
    jar=cookielib.CookieJar()
    cookie_handler=urllib2.HTTPCookieProcessor(jar)
    opener=urllib2.build_opener(cookie_handler)
    number=begin
    pattern=re.compile("\d+")
    file = opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=" + str(number))
    cookie_say=(list(jar)[0].value)
    number="44827"
    count=0
    while True:
        file=opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="+(number))
        content=file.read()
        numbers=re.findall(pattern,content)
        cookie_say+=(list(jar)[0].value)
        if(len(numbers)!=1):
            break
        number=numbers[0]
        count+=1
        print(count,number)
    print(cookie_say)

level2=True
if(level2==False):
    import bz2
    cookie_say=urllib.unquote_plus(cookie_say)
    #print(cookie_say)
    plain=bz2.decompress(cookie_say)
    print(plain)
    #is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.
    #Mozart's Father: https://en.wikipedia.org/wiki/Leopold_Mozart
    import level14
    print(level14.call("Leopold"))
    #VIOLIN

level3=False

jar = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(jar)
auth_handler = urllib2.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
opener = urllib2.build_opener(auth_handler,cookie_handler)
# url='http://www.pythonchallenge.com/pc/def/linkedlist.php'
# file=opener.open(url)
# print(file.read())
# print(list(jar))
#list(jar)[0].value = 'the+flowers+are+on+their+way'
jar.set_cookie(cookielib.Cookie(version=0, name='info', value='the+flowers+are+on+their+way', port=None, port_specified=False, domain='.pythonchallenge.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1487281544, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False))
print(list(jar))
url='http://www.pythonchallenge.com/pc/return/violin.html'
file=opener.open(url)
print(file.read())
print(list(jar))
url='http://www.pythonchallenge.com/pc/stuff/violin.php'
file=opener.open(url)
print(file.read())
print(list(jar))
#oh well, don't you dare to forget the balloons
#balloons