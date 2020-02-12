a = ['<td>2020-02-07</td>', '<td>2020-02-08</td>', '<td>2020-02-09</td>']
list = []
dict = {}

for b in a:
    n = 1
    c = b.split(">")[1].split("<")[0]
    if n == 1:
        dict["日期"] = c
    elif n == 2:
        dict["出生"] = c
    else:
        dict["生日"] = c
    n += 1
    list.append(dict)
print(list)

