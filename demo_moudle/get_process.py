import psutil

b = []
pids = psutil.pids()
for pid in pids:
    p = psutil.Process(pid)
    process_name = p.name()
    b.append(process_name)
print(b)


