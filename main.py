from json_to_elan import make_elan
from detector import detector

detector(data_path = 'entradas')

make_elan(data_dir = 'salidas')