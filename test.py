import requests
import json


id_simbolos = list()
simbolos = ['AGRO' , 'ALUA' , 'APBR' , 'AUSO' , 'BHIP' , 'BMA' , 'BOLT' , 'BPAT' ,
'BRIO' , 'BRIO6' , 'BYMA' , 'CADO' , 'CAPU' , 'CAPX' , 'CARC' , 'CECO2' ,
'CELU' , 'CEPU' , 'CGPA' , 'COLO' , 'COME' , 'CRES' , 'CGTM' , 'CTIO' ,
'CVH' , 'DGCU2' , 'DYCA' , 'EDN' , 'ESME' , 'FERR' , 'FIPL' , 'FRAN' ,
'GARO' , 'GBAN' , 'GCLA', 'GGAL' ,'GRIM' , 'HARG' , 'HAVA' , 'INAG' ,
'INDU' , 'INTR' , 'INVJ' , 'IRCP' , 'IRSA' , 'LEDE' , 'LOMA' , 'LONG',
'MERA' , 'METR' , 'MIRG' , 'MOLA' , 'MOLI' , 'MORI' , 'OEST' , 'PAMP',
'PATA' , 'PATY' , 'PESA' , 'PGR' , 'POLL' , 'PSUR' , 'REP' , 'RIGO' , 'RICH',
'ROSE','SAMI','SEMI','STD','SUPV','TECO2','TEF','TGLT','TGNO4','TGSU2','TRAN',
'TS','TXAR','VALO','YPFD']
for simbolo in simbolos:
    url_idTitulo = 'https://www.invertironline.com/api/cotizaciones/idtitulo?simbolo='+simbolo+'&mercado=BCBA'
    idTitulo = requests.get( url = url_idTitulo , headers = {
        'simbolo':simbolo,
        'mercado':'BCBA'
        } )
    id = str(idTitulo.text)
    url = "https://www.invertironline.com/Titulo/GraficoIntradiario?idTitulo="+id+"&idTipo=4&idMercado=1"
    dato = requests.get( url , headers = {
        'idTitulo': id,
        'idTipo': '4',
        'idMercado': '1'
        } )
    with open(simbolo+'.json', 'w') as file:
        json.dump(dato.text, file)
#print(dato.text)
