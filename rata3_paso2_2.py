import glob
import pymssql
import os
import lxml.html as LH
print("Rata 3 paso 2 by pohvak mayo 2018")
rutaLocal="/Users/pohvak/Documents/htmlsAplicaciones/"
if os.path.isfile(rutaLocal+"queryInserts.sql"):
    os.remove(rutaLocal+"queryInserts.sql")
archivo=open(rutaLocal+"queryInserts.sql","w")
conteo=len(glob.glob(rutaLocal+"*.html"))
c_ar=1
for htmlArticulo in glob.glob(rutaLocal+"*.html"):
    print("agregando query para "+os.path.basename(htmlArticulo)+" archivo "+str(c_ar)+" de "+str(conteo))
    tree = LH.parse(htmlArticulo)
    renglones=len([td.text_content() for td in tree.xpath('//tr')])
    for c in range (1,renglones+1):
        q="insert into tbPasoAplicaciones values ('"+str.replace(os.path.basename(htmlArticulo),'.html','')+"','" #nombre
        q+=str.replace(''.join([td.text_content() for td in tree.xpath('//tr['+str(c)+']/td[2]')]).strip(),"'","")+"','" #fabricante
        q+=str.replace(''.join([td.text_content() for td in tree.xpath('//tr['+str(c)+']/td[3]')]).strip()+''.join([td.text_content() for td in tree.xpath('//tr['+str(c)+']/td[4]')]).strip(),"'","")+"','" #modelo
        q+=str.replace(''.join([td.text_content() for td in tree.xpath('//tr['+str(c)+']/td[5]')]).strip(),"'","")+"','"  #submodelo
        q+=str.replace(''.join([td.text_content() for td in tree.xpath('//tr['+str(c)+']/td[1]')]).strip(),"'","")+"')" #anio
        archivo.write(q+'\n')
    c_ar+=1
archivo.close()
