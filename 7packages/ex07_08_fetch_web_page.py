# Web-sivun lataaminen

import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
content = f.read()
print(f"Tiedoston pituus on {len(content)} tavua.")
print(f"**Alku**:\n{content[:300]}")
print(f"**Loppu**:\n{content[-50:-1]}")
