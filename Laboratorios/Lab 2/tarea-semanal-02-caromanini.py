import csv

def import_data():
    print("Ingresar nombre del archivo: ")
    csv = input()
    
    list = []

    with open(csv) as myfile:
        firstline = True
        for i in myfile:
            if firstline:
                keys = i.replace('\n','').split(';')
                firstline = False

            else:
                values = i.replace('\n','').split(';')
                list.append({keys[j]: values[j] for j in range(len(keys))})

    return list

data = import_data()

def export_tables_by_region(data, tables_by_region):  
    tarapaca = 0
    antofa = 0
    atacama = 0
    coquimbo = 0
    valparaiso = 0
    ohiggins = 0
    maule = 0
    biobio = 0
    araucania = 0
    lagos = 0
    aysen = 0
    magallanes=0
    metropolitana = 0
    rios=0
    arica=0
    ñuble=0 

    for i in data:
        if i["RegiÃ³n"]=='DE TARAPACA':
            tarapaca+=1
        elif i["RegiÃ³n"]=='DE ANTOFAGASTA':
            antofa+=1
        elif i["RegiÃ³n"]=='DE ATACAMA':
            atacama+=1
        elif i["RegiÃ³n"]=='DE COQUIMBO':
            coquimbo+=1
        elif i["RegiÃ³n"]=='DE VALPARAISO':
            valparaiso+=1
        elif i["RegiÃ³n"]=="DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS":
             ohiggins+=1
        elif i["RegiÃ³n"]=='DEL MAULE':
            maule+=1
        elif i["RegiÃ³n"]=='DEL BIOBIO':
            biobio+=1
        elif i["RegiÃ³n"]=='DE LA ARAUCANIA':
            araucania+=1
        elif i["RegiÃ³n"]=='DE LOS LAGOS':
            lagos+=1
        elif i["RegiÃ³n"]=="DE AYSEN DEL GENERAL CARLOS IBAÃ‘EZ DEL CAMPO":
            aysen+=1
        elif i["RegiÃ³n"]=='DE MAGALLANES Y DE LA ANTARTICA CHILENA':
            magallanes+=1
        elif i["RegiÃ³n"]=='METROPOLITANA DE SANTIAGO':
            metropolitana+=1
        elif i["RegiÃ³n"]=='DE LOS RIOS':
            rios+=1
        elif i["RegiÃ³n"]=='DE ARICA Y PARINACOTA':
            arica+=1
        elif i["RegiÃ³n"]=="DE Ã‘UBLE":
            ñuble+=1

    tarapaca/=4
    antofa/=4
    atacama/=4
    coquimbo/=4
    valparaiso/=4
    ohiggins/=4
    maule/=4
    biobio/=4
    araucania/=4
    lagos/=4
    aysen/=4
    magallanes/=4
    metropolitana/=4
    rios/=4
    arica/=4
    ñuble/=4

    with open(tables_by_region, 'w') as file:
        file.write('DE TARAPACA;'+str(tarapaca)+'\n')
        file.write('DE ANTOFAGASTA;'+str(antofa)+'\n')
        file.write('DE ATACAMA;'+str(atacama)+'\n')
        file.write('DE COQUIMBO;'+str(coquimbo)+'\n')
        file.write('DE VALPARAISO;'+str(valparaiso)+'\n')
        file.write("DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS;"+str(ohiggins)+'\n')
        file.write('DEL MAULE;'+str(maule)+'\n')
        file.write('DEL BIOBIO;'+str(biobio)+'\n')
        file.write('DE LA ARAUCANIA;'+str(araucania)+'\n')
        file.write('DE LOS LAGOS;'+str(lagos)+'\n')
        file.write("DE AYSEN DEL GENERAL CARLOS IBAÃ‘EZ DEL CAMPO;"+str(aysen)+'\n')
        file.write('DE MAGALLANES Y DE LA ANTARTICA CHILENA;'+str(magallanes)+'\n')
        file.write('METROPOLITANA DE SANTIAGO;'+str(metropolitana)+'\n')
        file.write('DE LOS RIOS;'+str(rios)+'\n')
        file.write('DE ARICA Y PARINACOTA;'+str(arica)+'\n')
        file.write("DE Ã‘UBLE;"+str(ñuble)+'\n')

export_tables_by_region(data, 'tables_by_region.csv')

def export_general_results(data, general_results): 
    
    votos_boric = 0
    votos_kast = 0
    votos_nulos = 0
    votos_blanco = 0

    for i in data:
        if i["Candidato"]=="GABRIEL BORIC FONT":
            votos_boric+=int(i["Votos TRICEL"])
        elif  i["Candidato"]=="JOSE ANTONIO KAST RIST":
            votos_kast+=int(i["Votos TRICEL"])
        elif i["Candidato"]=="VOTOS NULOS":
           votos_nulos+=int(i["Votos TRICEL"])
        elif i["Candidato"]=="VOTOS EN BLANCO":
            votos_blanco+=int(i["Votos TRICEL"])

    with open(general_results,'w') as file:
        file.write('GABRIEL BORIC FONT;' + str(votos_boric) + '\n')
        file.write('JOSE ANTONIO KAST RIST;'+str(votos_kast)+'\n')
        file.write('VOTOS NULOS;'+str(votos_nulos)+'\n')
        file.write('VOTOS EN BLANCO;'+str(votos_blanco)+'\n')

export_general_results(data, 'general_results.csv')

def export_count_by_local(data, local_results):
    votos_boric=0
    votos_kast=0
    votos_nulo=0
    votos_blanco=0

    print("Ingresar nombre del local para analizar:")
    local=input()

    for i in data:
        if i["Local"]==str(local):
            if i["Candidato"]=="GABRIEL BORIC FONT":
                votos_boric+=int(i["Votos TRICEL"])
            elif i["Candidato"]=="JOSE ANTONIO KAST RIST":
                votos_kast+=int(i["Votos TRICEL"])
            elif i["Candidato"]=="VOTOS NULOS":
                votos_nulo+=int(i["Votos TRICEL"])
            elif i["Candidato"]=="VOTOS EN BLANCO":
                votos_blanco+=int(i["Votos TRICEL"])

    with open(local_results, 'w') as file:
        file.write('GABRIEL BORIC FONT;' + str(votos_boric) + '\n')
        file.write('JOSE ANTONIO KAST RIST;'+str(votos_kast)+'\n')
        file.write('VOTOS NULOS;'+str(votos_nulo)+'\n')
        file.write('VOTOS EN BLANCO;'+str(votos_blanco)+'\n')

export_count_by_local(data,'local_results.csv')