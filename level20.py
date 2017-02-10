import base64
import cookielib
import urllib2
import wave

has_wav_file=True
if has_wav_file==False:
    level_url = "http://www.pythonchallenge.com/pc/hex/bin.html"
    username = "butter"
    password = "fly"
    jar = cookielib.CookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(jar)
    auth_handler = urllib2.HTTPBasicAuthHandler()
    auth_handler.add_password('pluses and minuses', 'www.pythonchallenge.com', 'butter', 'fly')
    opener = urllib2.build_opener(auth_handler, cookie_handler)
    file=opener.open(level_url)
    content=file.read()
    content=content[635:]
    x=base64.b64decode(content)
    file = open("test.wav", "wb")
    file.write(x)
    file.close()

infile=wave.open("test.wav")
outfile1=wave.open("test1.wav","w")
outfile2=wave.open("test2.wav","w")
wave_params=infile.getparams()
outfile1.setparams(wave_params)
outfile2.setparams(wave_params)
assert(infile.getsampwidth()==2)
outfile1.setsampwidth(1)
outfile2.setsampwidth(1)
frames=infile.readframes(infile.getnframes())
outfile1.writeframes(frames[0::2])
outfile2.writeframes(frames[1::2])
infile.close()
outfile1.close()
outfile2.close()

#idiot
#http://www.pythonchallenge.com/pc/hex/idiot.html
