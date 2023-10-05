import csv, datetime

def dtcsvlog(*args):
    """
    Write a log message into a csv.
    """
    print(args)
    with open(str(datetime.date.today())+".csv", "a", newline = "") as csvfile:
        writer = csv.writer(csvfile, delimiter = ",")
        log = [datetime.datetime.now()]
        for arg in args:
            log.append(arg)
        writer.writerow(log)
    return