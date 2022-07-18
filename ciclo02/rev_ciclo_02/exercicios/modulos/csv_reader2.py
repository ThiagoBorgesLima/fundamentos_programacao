import csv


def read_file(file):
    content = []

    with open(file, 'r', ) as f:
        reader = csv.DictReader(f)

        for line in reader:
            content.append(line)

    return content