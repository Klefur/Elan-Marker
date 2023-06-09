from json_to_elan import make_elan
from detector import detector

detector(data_path = "input", filters=["d", "t"])

make_elan(data_dir = 'output')