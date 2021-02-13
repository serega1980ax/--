my_list = ["Привет всем", "МоРЕ", "ОКеАн"]
def lower(a):
    a = a.lower()
    return a
c = list(map(lambda x: x.lower(), my_list))
print(",".join(c))

my_list = ["Привет всем", "МоРЕ", "ОКеАн"]
def upper(b):
    b = b.upper()
    return b
d = list(map(lambda x: x.upper(), my_list))
print(",".join(d))

