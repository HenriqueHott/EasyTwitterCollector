import json

def get_configs():
    return json.load(open('config.json'))

def check_coordinates_format(coordinates):
    return True


def check_date_format():
    pass


def count_file_lines(file):
    line_counter = 0

    with open(file, encoding='utf8', mode='r') as f:
        for i in f:
            line_counter += 1

    return line_counter


def indent_json(data, out=None, encondig='utf8'):
    if out:
        json.dump(data, open(out, mode='w', encoding=encondig), ensure_ascii=False, indent=4)

    else:
        return json.dumps(data, ensure_ascii=False, indent=4)
