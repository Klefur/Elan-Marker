import json
import glob

NANOSECONDS_PER_SECOND = 1e9

def detector(data_path: str = "entradas"):
    textoSalida = []
    json_files = glob.glob(data_path + "/*.json", recursive=False)
    for file_path in json_files:
        with open('entradas/in.json', encoding='utf-8') as json_file:
            jsonSalida = open(f'salidas/{file_path[8:-5]}_out.json', 'w', encoding='utf-8')
            data = json.load(json_file)
            
            for info in data:
                for word in info['NBest'][0]['Words']:
                    inicio = round(word['Offset']*100/NANOSECONDS_PER_SECOND, 2) 
                    fin = round(inicio + word['Duration']*100/NANOSECONDS_PER_SECOND, 2)
                    textoSalida.append({'text': word['Word'], 'timestamp': [inicio, fin]})
            textoSalida = json.dumps(textoSalida, indent=4, ensure_ascii=False)
            jsonSalida.write(textoSalida)
            jsonSalida.close()