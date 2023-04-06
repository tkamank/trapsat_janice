import csv

def write_csv_data(filename, data):
    with open(filename, 'a') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(data)