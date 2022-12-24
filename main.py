import os
import csv

def list_files(root_dir):
    file_list = []

    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(root_dir):
        # Get the client name from the first level subfolder
        client_name = os.path.basename(os.path.dirname(root))

        # Get the week number and delivery number from the second and third level subfolders
        week_number = os.path.basename(os.path.dirname(root))
        delivery_number = os.path.basename(root)

        # Add the file name, client name, week number, delivery number, and full path
        # to the file to the file list
        for file in files:
            client_name = os.path.relpath(os.path.join(root, file), root_dir).split("\\", 1)[0]
            file_list.append([file, client_name, week_number, delivery_number, os.path.relpath(os.path.join(root, file), root_dir)])

    return file_list

def write_to_csv(file_list, csv_file):
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        # Add a header row
        writer.writerow(["Filename", "Client Name", "Week Number", "Delivery Number", "Path"])
        writer.writerows(file_list)

root_dir = r'C:\Users\mega\Documents\sandbox\list-files-in-excel\drive-download-20221224T164507Z-002'
csv_file = r'C:\Users\mega\Documents\sandbox\list-files-in-excel\output\output.csv'

file_list = list_files(root_dir)
write_to_csv(file_list, csv_file)
