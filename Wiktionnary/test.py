

import urllib.request
opener = urllib.request.FancyURLopener({})
print(str(opener.open(url).read()))