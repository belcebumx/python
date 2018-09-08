import urllib.request
prefijo="8003"
for a in range (1000):
    try:
        print("buscando pedimento "+prefijo+str(a).zfill(3))
        guardarEn="/Users/pohvak/Documents/almacenPython/pedimentos/"+prefijo+str(a).zfill(3)+".pdf"
        urllib.request.urlretrieve("http://aasavinon.no-ip.org/Archivo/Pedimentos/SV01%201623%20230%20"+prefijo+str(a).zfill(3)+".PDF",guardarEn)
        print("pedimento "+prefijo+str(a).zfill(3)+"                 guardado")
    except Exception:
        continue
