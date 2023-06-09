import json
import glob


NANOSECONDS_PER_SECOND = 1e9

def apply_filter(text: str, filters: list):
    """
    filters : list of strings
    """

    for filter in filters:
        if (filter in text):
            return True
    return False


def detector(data_path: str = "input", filters: list = []):
    """
    data_path : relative path for the folder that contains the input .json files
    filters : list of strings
    """

    output_text = []
    # Get every .json file from data_path folder
    json_files = glob.glob(data_path + "\*.json", recursive=False)
    for file_path in json_files:
        with open(f'{file_path}', encoding='utf-8') as json_file:
            # Making .json output
            json_file_name = file_path[len(data_path)+1:-5]
            json_output = open(f'output\{json_file_name}_out.json', 'w', encoding='utf-8')

            # Reading data
            data = json.load(json_file)
            for info in data:
                for word in info['NBest'][0]['Words']:
                    # Saving only if word contains any filter
                    if (apply_filter(word['Word'], filters)):
                        start = round(word['Offset']*100/NANOSECONDS_PER_SECOND, 2) 
                        end = round(start + word['Duration']*100/NANOSECONDS_PER_SECOND, 2)
                        output_text.append({'text': word['Word'], 'timestamp': [start, end]})

            json_output.write(json.dumps(output_text, indent=4, ensure_ascii=False))
            json_output.close()