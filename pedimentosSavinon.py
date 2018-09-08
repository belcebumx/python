import urllib.request
numeros=["0","1","2","3","4","5","6","7","8","9"]
numerosParaPrefijo=["0","1","2","3","4","5","6","7","8","9"]
rutaURL="http://aasavinon.no-ip.org/Archivo/Pedimentos/"
for numeroPP in numeros:
    for numeroP in numerosParaPrefijo:
        prefijo="8003"+str(numeroPP)+str(numeroP)
        for numero in numeros:
            try:
                print("buscando pedimento "+prefijo+numero)
                guardarEn="/Users/pohvak/Documents/almacenPython/pedimentos/"+str(prefijo)+str(numero)+".pdf"
                urllib.request.urlretrieve(rutaURL+"SV01%201623%20230%20"+str(prefijo)+str(numero)+".PDF",guardarEn)
                print("pedimento "+prefijo+numero+"                                         guardado")
            except Exception:
                continue
