
def load_dict():
    with open("terms.csv") as f:
        d = {}
        for l in f:
            l = l.strip()
            if len(l) > 0 and l[0] != '#':
                fields = l.split(";")
                for i in range(3):
                    fields[i] = fields[i].strip()
                for k in fields[0].split(","):
                    for v in fields[1].split(","):
                        d.setdefault(k.strip(),[]).append(v.strip())
    return d

d = load_dict()
print(d["interpretator"])
print(d["nyckelord"])


