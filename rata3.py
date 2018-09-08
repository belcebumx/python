from lxml import etree
from pathlib import Path
import urllib
import getpass
import os
import pymssql
import subprocess
from urllib.request import urlretrieve
rutaLocal="/Users/pohvak/Documents/htmlsAplicaciones/"
server = input ("servidor: ")
user= input("usuario: ")
password=getpass.getpass("contrasenia: ")
rutaURL="https://uacparts.com/Catalog/Buyers?part="
conn = pymssql.connect(server, user, password, "dbSIA")
cursor = conn.cursor()
query="select replace(apr.CodigoArticuloProveedor,' ','%20')+'.html' from tbarticulos art,tbArticulosProveedores apr,tbAlmacenes alm "
query+="where art.idArticulo=apr.idArticulo and alm.idArticulo=art.idArticulo and alm.idSucursal=1 and alm.idAlmacenTipo=1 "
query+=" and apr.idProveedor=275 and len(apr.CodigoArticuloProveedor)>3 order by replace(apr.CodigoArticuloProveedor,' ','%20')+'.html' "
print("conectando a la base de datos...")
sobreescribir=input("¿deseas sobreescribir los archivos existentes S / N")
cursor.execute(query)
row = cursor.fetchone() 
while row:
    archivo = Path(rutaLocal+row[0])
    if archivo.is_file():
        if sobreescribir=="S":
            print("descargando archivo %s" % (row[0]))
            guardarEn=rutaLocal+row[0]
            urllib.request.urlretrieve(rutaURL+row[0],guardarEn)
            f=open(guardarEn,'r')
        else:
            print("omiti el archivo %s porque ya lo tengo" % (row[0]))
    else:
        print("descargando archivo %s" % (row[0]))
        guardarEn=rutaLocal+row[0]
        urllib.request.urlretrieve(rutaURL+row[0],guardarEn)
        f=open(guardarEn,'r')
    row = cursor.fetchone()
conn.close()
