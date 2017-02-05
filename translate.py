import os
import csv
import config

def get_value(label):
    translation = label
    filename = os.path.join('static', config.CSV_FILE)

    try:
        with open(filename, 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            translate_dict = dict(reader)
            translation = translate_dict.get(label, label)

    except OSError:
        pass

    return translation

