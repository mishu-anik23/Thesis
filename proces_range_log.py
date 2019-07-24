import csv
import datetime
import os
import time


def csv_read_from_file(filepath):
    with open(filepath) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            yield row


if __name__ == '__main__':
    filename = 'wimodlr_rng_status_2019-07-20_20-27-11_LoRa SF9_LoRa BW 800.log'
    rel_path = os.path.relpath(filename)
    print(rel_path)
    infilepath = os.path.join(os.getcwd(), 'data', 'range_log', 'master2slave', filename)
    print(infilepath)
    print(os.path.relpath(infilepath), os.getcwd())
    row = csv_read_from_file(infilepath)
    t1 = next(row)['Host Time']
    t1_s = datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S").timestamp()
    print(t1_s)
    t2 = next(row)['Host Time']
    t2_s = datetime.datetime.strptime(t2, "%Y-%m-%d %H:%M:%S").timestamp()
    print(t2_s)
    print(t2_s - t1_s)

    print(t1)
    print(t2)
    print(time.ctime(time.time()))
    print(next(row))
    print(next(row))
    print(next(row))