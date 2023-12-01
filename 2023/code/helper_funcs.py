def read_input_file(file_name):
    with open(f'../inputs/{file_name}', 'r') as f:
        file_string = f.read()
    return file_string


def parse_input_into_list(file_string, ignore_blank_rows=True):
    if ignore_blank_rows:
        records = [r for r in file_string.split('\n') if r.strip()]
    else:
        records = [r for r in file_string.split('\n')]

    return records
