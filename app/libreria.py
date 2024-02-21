
import csv


def DataLoad(ruta):    
    with open(ruta, 'r') as csvfile:

        lineas= csv.reader(csvfile, delimiter=',')
        header = next(lineas)
        data=[]
        for row in lineas:
            iterable=zip(header, row)
            dict = {key: value for key, value in iterable} 
            data.append(dict)         
    return data

def selePais(NombrePais, datos):
    for i in datos:
        if i['Country/Territory']==NombrePais.capitalize():

           dic= { 
            '2022': int(i['2022 Population']),
            '2020': int(i['2020 Population']),
            '2015': int(i['2015 Population']),
            '2010': int(i['2010 Population']),
            '2000': int(i['2000 Population']),
            '1990': int(i['1990 Population']),
            '1980': int(i['1980 Population']),
            '1970': int(i['1970 Population']),
            }
    return dic

def DataLoad2(ruta):    
    with open(ruta, 'r') as csvfile:

        lineas= csv.reader(csvfile, delimiter=',')
        dato = next(lineas)
        pais = dato.index('Country/Territory')
        densidad=dato.index('World Population Percentage')
        paises=[]
        densidades=[]
        for i in lineas:
            densidades.append(i[densidad])
            paises.append(i[pais])      
        
    return paises, densidades

if __name__ == '__main__':

    
        ruta="./data.csv"

        datos=DataLoad(ruta)

        NombrePais=input('ingrese el pais a graficar: ')

        print(selePais(NombrePais,datos))



