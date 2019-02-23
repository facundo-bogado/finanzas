import requests

simbolos = []
with open('bonos.txt', 'r') as f:
    lineas = [linea.split() for linea in f]

for linea in lineas[0]:
    simbolos.append(linea)
print(simbolos)

def peticionar_datos(simbolos):
    id_simbolos = list()
    for simbolo in simbolos:
        url_idTitulo = 'https://www.invertironline.com/api/cotizaciones/idtitulo?simbolo='+simbolo+'&mercado=BCBA'
        idTitulo = requests.get( url = url_idTitulo , headers = {
            'simbolo':simbolo,
            'mercado':'BCBA'
            } )
        id = str(idTitulo.text)
        url = "https://www.invertironline.com/Titulo/FundamentalesTecnicosBonos"
        dato = requests.post( url , data = {
            'id':id
            } )
        with open(simbolo+'.html', 'w') as file:
            file.write(dato.text)

peticionar_datos(simbolos)
