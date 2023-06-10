import json
import glob

NANOSECONDS_PER_SECOND = 1e9

def apply_filter(text: str, filters: list):
    """
    filters : list of strings
    """

    for filter in filters:
        if (filter in text.casefold()):
            return True
    return False

def filter_json(data_path: str = "input", filters: list = []):
    """
    data_path : relative path for the folder that contains the input .json files
    filters : list of strings
    """

    # Get every .json file from data_path folder
    json_files = glob.glob(data_path + "\*.json", recursive=False)
    for file_path in json_files:
        output_text = []
        with open(f'{file_path}', encoding='utf-8') as json_file:
            # Making .json output
            json_file_name = file_path[len(data_path)+1:-5]
            json_output = open(f'output\{json_file_name}.json', 'w', encoding='utf-8')

            # Reading data
            data = json.load(json_file)
            for segment in data["segments"]:
                for word in segment["words"]:
                    # Saving only if word contains any filter
                    if (apply_filter(word['text'], filters)):
                        output_text.append({'text': word['text'],
                                            'timestamp': [word['start'], word['end']]})

            json_output.write(json.dumps(output_text, indent=4, ensure_ascii=False))
            json_output.close()