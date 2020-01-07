import psutil

pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    process_name = p.name()
    print("Process name is: %s, pid is: %s" % (process_name, pid))


