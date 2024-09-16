
# d = {}
# d["arsoitenars"].append("test")
# print(d)

f = open("terms.csv")
lines = f.readlines()
d = {}
for l in lines:
    l = l.strip()
    if len(l) > 0 and l[0] != '#':
        fields = l.split(";")
        for i in range(3):
            fields[i] = fields[i].strip()
        for k in fields[0].split(","):
            for v in fields[1].split(","):
                d.setdefault(k.strip(),[]).append(v.strip())
print(d["interpretator"])
print(d["nyckelord"])


