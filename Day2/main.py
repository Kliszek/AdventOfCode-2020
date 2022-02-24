rows = list()



for x in range(0,1000):
    rows.append(input().strip("\n"))

data = {
  "range1": list(int(x.split("-")[0]) for x in rows),
  "range2": list(int(x.split(" ")[0].split("-")[1]) for x in rows),
  "char": list(x.split(":")[0][-1] for x in rows),
  "password": list(x.split(" ")[2] for x in rows)
}

print(data["range1"][0])
print(data["range2"][0])
print(data["char"][0])
print(data["password"][0])

correct=0
for x in range(len(rows)):
    cond1 = data["password"][x][data["range1"][x]-1]==data["char"][x]
    cond2 = data["password"][x][data["range2"][x]-1]==data["char"][x]
    if cond1 != cond2:
        correct+=1

print(correct)