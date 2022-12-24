import os
import csv

def list_files(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def write_to_csv(file_list, csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([[f] for f in file_list])

folder = '/path/to/folder'
csv_file = '/path/to/output.csv'

file_list = list_files(folder)
write_to_csv(file_list, csv_file)
