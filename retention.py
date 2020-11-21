import os
import time
import shutil

d = {}
with open("sample_input_file.config") as f:
    for line in f:
        (key, value) = line.rstrip("\n").split("=")
        if value.isdigit():
            d[key] = int(value)
        else:
            d[key] = value


def remove_log_dir(log_dir_path, log_period, now):
    for r,d,f in os.walk(log_dir_path):
        for dir in d:
            filestamp = os.path.getmtime(os.path.join(r,dir))
            filecmp = now - (log_period * 86400)
            if filestamp < filecmp:
                print "removing", os.path.join(r,dir)
                shutil.rmtree(os.path.join(r,dir))
            else:
                print "no old directories"


def remove_csv_file(csv_file_path, csv_period, now):
    for r,d,f in os.walk(csv_file_path):
        for file in f:
            filestamp = os.path.getmtime(os.path.join(r,file))
            filecmp = now - (csv_period * 86400)
            if filestamp < filecmp:
                print "removing", os.path.join(r,file)
                os.remove(os.path.join(r,file))
            else:
                print 'no old files'



log_dir_path = d.get('log_file_path')
log_period = d.get('log_file_retention_period')
csv_file_path = d.get('csv_file_path')
csv_period = d.get('csv_file_retention_period')
now = time.time()
remove_log_dir(log_dir_path, log_period, now)
remove_csv_file(csv_file_path, csv_period, now)

