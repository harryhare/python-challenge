import string
level_url="http://www.pythonchallenge.com/pc/hex/bonus.html"

crypt="va gur snpr bs jung?"
alphbet=string.ascii_lowercase
for i in range(1,26):
    x = string.maketrans( alphbet,alphbet[i:]+alphbet[:i])
    print(crypt.translate(x))
# in the face of what?

import this